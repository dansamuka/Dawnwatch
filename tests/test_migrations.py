from alembic import command
from alembic.config import Config
from sqlalchemy import create_engine, inspect


def test_initial_migration_upgrades_cleanly(tmp_path) -> None:
    database_path = tmp_path / "dawnwatch.db"
    config = Config("alembic.ini")
    config.set_main_option("sqlalchemy.url", f"sqlite:///{database_path}")

    command.upgrade(config, "head")

    engine = create_engine(f"sqlite:///{database_path}")
    tables = set(inspect(engine).get_table_names())
    assert {
        "entities",
        "entity_aliases",
        "observations",
        "evidence",
        "relationships",
        "indicators",
        "risk_snapshots",
    }.issubset(tables)
