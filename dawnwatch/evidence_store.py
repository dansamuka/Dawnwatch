from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path


@dataclass(frozen=True)
class StoredEvidence:
    sha256: str
    content_path: Path
    manifest_path: Path
    size_bytes: int


class LocalEvidenceStore:
    """Content-addressed local evidence store.

    Raw evidence bytes are immutable. Metadata is written alongside the object in a JSON
    manifest. Re-storing identical bytes returns the same content path.
    """

    def __init__(self, root: str | Path):
        self.root = Path(root)

    def put(
        self,
        content: bytes,
        *,
        source_name: str,
        source_url: str | None = None,
        observed_at: datetime | None = None,
        mime_type: str = "application/octet-stream",
    ) -> StoredEvidence:
        digest = hashlib.sha256(content).hexdigest()
        shard = self.root / digest[:2] / digest[2:4]
        content_path = shard / digest
        manifest_path = shard / f"{digest}.json"
        shard.mkdir(parents=True, exist_ok=True)

        if not content_path.exists():
            content_path.write_bytes(content)

        if not manifest_path.exists():
            manifest = {
                "sha256": digest,
                "size_bytes": len(content),
                "source_name": source_name,
                "source_url": source_url,
                "observed_at": (observed_at or datetime.now(timezone.utc)).isoformat(),
                "mime_type": mime_type,
            }
            manifest_path.write_text(
                json.dumps(manifest, indent=2, sort_keys=True),
                encoding="utf-8",
            )

        return StoredEvidence(
            sha256=digest,
            content_path=content_path,
            manifest_path=manifest_path,
            size_bytes=len(content),
        )
