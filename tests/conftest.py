import json
from pathlib import Path
from unittest.mock import patch

import pytest
from typer.testing import CliRunner

from gandi_cli.config import GandiConfig, AuthConfig, DefaultsConfig


@pytest.fixture
def cli_runner():
    return CliRunner()


@pytest.fixture
def mock_config():
    config = GandiConfig(
        auth=AuthConfig(pat="test-token-123"),
        defaults=DefaultsConfig(sharing_id="test-org-id", output="table"),
    )
    with patch("gandi_cli.main.load_config", return_value=config):
        yield config


def load_fixture(name: str) -> dict | list:
    fixture_path = Path(__file__).parent / "fixtures" / name
    return json.loads(fixture_path.read_text())
