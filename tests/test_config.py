"""Tests for gandi_cli.config module."""

from __future__ import annotations

import os
import click
from pathlib import Path
from unittest.mock import patch

import pytest
import typer

from gandi_cli.config import (
    AuthConfig,
    DefaultsConfig,
    GandiConfig,
    get_token,
    load_config,
    save_config,
)


@pytest.fixture
def tmp_config_dir(tmp_path: Path):
    """Patch get_config_path to use a temporary directory."""
    with patch("gandi_cli.config.get_config_path", return_value=tmp_path):
        yield tmp_path


class TestLoadConfig:
    def test_load_config_no_file_returns_defaults(self, tmp_config_dir: Path):
        """When no config file exists, load_config returns default values."""
        config = load_config()
        assert config.auth.pat == ""
        assert config.defaults.sharing_id == ""
        assert config.defaults.output == "table"

    def test_save_and_load_roundtrip(self, tmp_config_dir: Path):
        """Saving a config and loading it back should return the same values."""
        original = GandiConfig(
            auth=AuthConfig(pat="my-secret-token"),
            defaults=DefaultsConfig(sharing_id="org-123", output="json"),
        )
        save_config(original)

        loaded = load_config()
        assert loaded.auth.pat == "my-secret-token"
        assert loaded.defaults.sharing_id == "org-123"
        assert loaded.defaults.output == "json"


class TestGetToken:
    def test_get_token_from_config(self, tmp_config_dir: Path):
        """get_token should return the token from the config file."""
        config = GandiConfig(auth=AuthConfig(pat="config-token"))
        save_config(config)

        token = get_token()
        assert token == "config-token"

    def test_get_token_env_var_overrides_config(self, tmp_config_dir: Path):
        """GANDI_PAT env var should take priority over config file."""
        config = GandiConfig(auth=AuthConfig(pat="config-token"))
        save_config(config)

        with patch.dict(os.environ, {"GANDI_PAT": "env-token"}):
            token = get_token()
        assert token == "env-token"

    def test_get_token_override_takes_priority(self, tmp_config_dir: Path):
        """An explicit override argument should take highest priority."""
        config = GandiConfig(auth=AuthConfig(pat="config-token"))
        save_config(config)

        with patch.dict(os.environ, {"GANDI_PAT": "env-token"}):
            token = get_token(override="override-token")
        assert token == "override-token"

    def test_get_token_raises_when_no_token(self, tmp_config_dir: Path):
        """get_token should raise typer.Exit when no token is available."""
        # Ensure GANDI_PAT is not set
        env = os.environ.copy()
        env.pop("GANDI_PAT", None)
        with patch.dict(os.environ, env, clear=True):
            with pytest.raises((SystemExit, click.exceptions.Exit)):
                get_token()
