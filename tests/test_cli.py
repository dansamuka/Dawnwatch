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


def test_validate_archive_cli(monkeypatch, capsys) -> None:
    monkeypatch.setattr("sys.argv", ["dawnwatch", "validate-archive"])
    main()
    output = json.loads(capsys.readouterr().out)
    assert output["valid"] is True
    assert output["case_count"] == 20


def test_benchmark_all_cli(monkeypatch, capsys) -> None:
    monkeypatch.setattr("sys.argv", ["dawnwatch", "benchmark-all"])
    main()
    output = json.loads(capsys.readouterr().out)
    assert len(output) == 5
    results = {item["case_id"]: item for item in output}
    assert results["kenya-cbex-2026"]["lead_time_days"] == 512
