from dawnwatch.evidence_store import LocalEvidenceStore


def test_identical_evidence_is_content_addressed(tmp_path) -> None:
    store = LocalEvidenceStore(tmp_path)
    first = store.put(b"same evidence", source_name="test")
    second = store.put(b"same evidence", source_name="test")
    assert first.sha256 == second.sha256
    assert first.content_path == second.content_path
    assert first.content_path.read_bytes() == b"same evidence"
