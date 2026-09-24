from sqlalchemy import inspect

from dawnwatch.persistence import create_schema


def test_core_schema_is_created() -> None:
    engine = create_schema()
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
