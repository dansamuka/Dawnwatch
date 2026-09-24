import tomllib
from pathlib import Path


def test_pyproject_is_valid_toml_and_registers_cli() -> None:
    data = tomllib.loads(Path("pyproject.toml").read_text(encoding="utf-8"))
    assert data["project"]["name"] == "dawnwatch"
    assert data["project"]["scripts"]["dawnwatch"] == "dawnwatch.cli:main"
