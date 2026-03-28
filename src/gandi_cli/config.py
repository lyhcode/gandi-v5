"""Configuration management for gandi-cli."""

from __future__ import annotations

import os
import sys
from pathlib import Path
from typing import Literal

import tomli_w
import typer
from pydantic import BaseModel
from platformdirs import user_config_dir

if sys.version_info >= (3, 11):
    import tomllib
else:
    try:
        import tomllib
    except ModuleNotFoundError:
        import tomli as tomllib


class AuthConfig(BaseModel):
    pat: str = ""


class DefaultsConfig(BaseModel):
    sharing_id: str = ""
    output: Literal["table", "json", "plain"] = "table"


class GandiConfig(BaseModel):
    auth: AuthConfig = AuthConfig()
    defaults: DefaultsConfig = DefaultsConfig()


def get_config_path() -> Path:
    """Return the path to the config directory."""
    return Path(user_config_dir("gandi-cli"))


def load_config() -> GandiConfig:
    """Load configuration from the TOML config file.

    Returns a default GandiConfig if the file does not exist.
    """
    config_file = get_config_path() / "config.toml"
    if not config_file.exists():
        return GandiConfig()
    with open(config_file, "rb") as f:
        data = tomllib.load(f)
    return GandiConfig(**data)


def save_config(config: GandiConfig) -> None:
    """Write configuration to the TOML config file."""
    config_dir = get_config_path()
    config_dir.mkdir(parents=True, exist_ok=True)
    config_file = config_dir / "config.toml"
    with open(config_file, "wb") as f:
        tomli_w.dump(config.model_dump(), f)


def get_token(override: str | None = None) -> str:
    """Resolve the API token with priority: override > GANDI_PAT env > config file.

    Raises typer.Exit if no token is found.
    """
    if override:
        return override
    env_token = os.environ.get("GANDI_PAT")
    if env_token:
        return env_token
    config = load_config()
    if config.auth.pat:
        return config.auth.pat
    typer.echo("Error: No API token found. Set GANDI_PAT env var, use --token, or run 'gandi-v5 auth login'.", err=True)
    raise typer.Exit(code=1)


def get_sharing_id(override: str | None = None) -> str | None:
    """Resolve the sharing ID with priority: override > GANDI_SHARING_ID env > config file."""
    if override:
        return override
    env_sharing_id = os.environ.get("GANDI_SHARING_ID")
    if env_sharing_id:
        return env_sharing_id
    config = load_config()
    return config.defaults.sharing_id or None


def get_output_format(override: str | None = None) -> str:
    """Resolve the output format with priority: override > config file."""
    if override:
        return override
    config = load_config()
    return config.defaults.output
