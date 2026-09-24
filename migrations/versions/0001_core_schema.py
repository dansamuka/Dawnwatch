"""Create Dawnwatch core intelligence schema.

Revision ID: 0001_core_schema
Revises:
Create Date: 2026-09-24
"""

from __future__ import annotations

import sqlalchemy as sa
from alembic import op


revision = "0001_core_schema"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "entities",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("entity_type", sa.String(length=64), nullable=False),
        sa.Column("canonical_name", sa.String(length=512), nullable=False),
        sa.Column("normalized_name", sa.String(length=512), nullable=False),
        sa.Column("status", sa.String(length=64), nullable=False),
        sa.Column("country", sa.String(length=3), nullable=True),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=False),
    )
    op.create_index("ix_entities_entity_type", "entities", ["entity_type"])
    op.create_index("ix_entities_canonical_name", "entities", ["canonical_name"])
    op.create_index("ix_entities_normalized_name", "entities", ["normalized_name"])

    op.create_table(
        "entity_aliases",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("entity_id", sa.Integer(), sa.ForeignKey("entities.id"), nullable=False),
        sa.Column("alias", sa.String(length=512), nullable=False),
        sa.Column("alias_type", sa.String(length=64), nullable=False),
        sa.Column("first_seen", sa.DateTime(timezone=True), nullable=True),
        sa.Column("last_seen", sa.DateTime(timezone=True), nullable=True),
    )
    op.create_index("ix_entity_aliases_entity_id", "entity_aliases", ["entity_id"])
    op.create_index("ix_entity_aliases_alias", "entity_aliases", ["alias"])

    op.create_table(
        "observations",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("source_name", sa.String(length=255), nullable=False),
        sa.Column("source_type", sa.String(length=64), nullable=False),
        sa.Column("source_tier", sa.String(length=1), nullable=False),
        sa.Column("source_url", sa.Text(), nullable=True),
        sa.Column("published_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column("observed_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("content_hash", sa.String(length=64), nullable=False, unique=True),
        sa.Column("content_type", sa.String(length=64), nullable=False),
        sa.Column("language", sa.String(length=16), nullable=True),
        sa.Column("metadata_json", sa.JSON(), nullable=False),
    )
    op.create_index("ix_observations_source_name", "observations", ["source_name"])
    op.create_index("ix_observations_source_type", "observations", ["source_type"])
    op.create_index("ix_observations_source_tier", "observations", ["source_tier"])
    op.create_index("ix_observations_observed_at", "observations", ["observed_at"])
    op.create_index("ix_observations_content_hash", "observations", ["content_hash"])

    op.create_table(
        "evidence",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("observation_id", sa.Integer(), sa.ForeignKey("observations.id"), nullable=False),
        sa.Column("evidence_key", sa.String(length=128), nullable=False, unique=True),
        sa.Column("sha256", sa.String(length=64), nullable=False),
        sa.Column("storage_uri", sa.Text(), nullable=False),
        sa.Column("review_status", sa.String(length=32), nullable=False),
        sa.Column("notes", sa.Text(), nullable=True),
    )
    op.create_index("ix_evidence_observation_id", "evidence", ["observation_id"])
    op.create_index("ix_evidence_evidence_key", "evidence", ["evidence_key"])
    op.create_index("ix_evidence_sha256", "evidence", ["sha256"])

    op.create_table(
        "relationships",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("source_entity_id", sa.Integer(), sa.ForeignKey("entities.id"), nullable=False),
        sa.Column("target_entity_id", sa.Integer(), sa.ForeignKey("entities.id"), nullable=False),
        sa.Column("relationship_type", sa.String(length=64), nullable=False),
        sa.Column("confidence", sa.Float(), nullable=False),
        sa.Column("first_seen", sa.DateTime(timezone=True), nullable=True),
        sa.Column("last_seen", sa.DateTime(timezone=True), nullable=True),
        sa.Column("review_status", sa.String(length=32), nullable=False),
        sa.Column("evidence_ids", sa.JSON(), nullable=False),
    )
    op.create_index("ix_relationships_source_entity_id", "relationships", ["source_entity_id"])
    op.create_index("ix_relationships_target_entity_id", "relationships", ["target_entity_id"])
    op.create_index("ix_relationships_relationship_type", "relationships", ["relationship_type"])

    op.create_table(
        "indicators",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("scheme_entity_id", sa.Integer(), sa.ForeignKey("entities.id"), nullable=False),
        sa.Column("indicator_type", sa.String(length=128), nullable=False),
        sa.Column("severity", sa.String(length=32), nullable=False),
        sa.Column("status", sa.String(length=32), nullable=False),
        sa.Column("confidence", sa.Float(), nullable=False),
        sa.Column("first_seen", sa.DateTime(timezone=True), nullable=False),
        sa.Column("last_seen", sa.DateTime(timezone=True), nullable=True),
        sa.Column("evidence_ids", sa.JSON(), nullable=False),
    )
    op.create_index("ix_indicators_scheme_entity_id", "indicators", ["scheme_entity_id"])
    op.create_index("ix_indicators_indicator_type", "indicators", ["indicator_type"])
    op.create_index("ix_indicators_first_seen", "indicators", ["first_seen"])

    op.create_table(
        "risk_snapshots",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("scheme_entity_id", sa.Integer(), sa.ForeignKey("entities.id"), nullable=False),
        sa.Column("snapshot_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("risk_state", sa.String(length=64), nullable=False),
        sa.Column("internal_score", sa.Integer(), nullable=False),
        sa.Column("active_indicator_count", sa.Integer(), nullable=False),
        sa.Column("explanation_json", sa.JSON(), nullable=False),
    )
    op.create_index("ix_risk_snapshots_scheme_entity_id", "risk_snapshots", ["scheme_entity_id"])
    op.create_index("ix_risk_snapshots_snapshot_at", "risk_snapshots", ["snapshot_at"])
    op.create_index("ix_risk_snapshots_risk_state", "risk_snapshots", ["risk_state"])


def downgrade() -> None:
    op.drop_table("risk_snapshots")
    op.drop_table("indicators")
    op.drop_table("relationships")
    op.drop_table("evidence")
    op.drop_table("observations")
    op.drop_table("entity_aliases")
    op.drop_table("entities")
