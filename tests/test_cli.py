import json

from dawnwatch.cli import main


def test_archive_search_cli(monkeypatch, capsys) -> None:
    monkeypatch.setattr(
        "sys.argv",
        ["dawnwatch", "archive-search", "QVSE"],
    )
    main()
    output = json.loads(capsys.readouterr().out)
    assert output[0]["case_id"] == "kenya-qvse-2026"
