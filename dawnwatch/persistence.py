from __future__ import annotations

from datetime import UTC, datetime
from enum import StrEnum
from typing import Any

from sqlalchemy import (
    JSON,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    String,
    Text,
    create_engine,
)
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, relationship, sessionmaker


class Base(DeclarativeBase):
    pass


def utcnow() -> datetime:
    return datetime.now(UTC)


class EntityType(StrEnum):
    SCHEME = "scheme"
    COMPANY = "company"
    PERSON = "person"
    DOMAIN = "domain"
    WEBSITE = "website"
    APP = "app"
    PHONE = "phone"
    EMAIL = "email"
    SOCIAL_ACCOUNT = "social_account"
    MESSAGING_CHANNEL = "messaging_channel"
    WALLET = "wallet"
    PAYBILL = "paybill"
    TILL = "till"
    ADDRESS = "address"
    REGULATOR = "regulator"
    LICENCE = "licence"
    COURT_CASE = "court_case"


class EntityRecord(Base):
    __tablename__ = "entities"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    entity_type: Mapped[str] = mapped_column(String(64), index=True)
    canonical_name: Mapped[str] = mapped_column(String(512), index=True)
    normalized_name: Mapped[str] = mapped_column(String(512), index=True)
    status: Mapped[str] = mapped_column(String(64), default="active")
    country: Mapped[str | None] = mapped_column(String(3), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=utcnow)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=utcnow, onupdate=utcnow
    )

    aliases: Mapped[list["EntityAliasRecord"]] = relationship(
        back_populates="entity", cascade="all, delete-orphan"
    )


class EntityAliasRecord(Base):
    __tablename__ = "entity_aliases"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    entity_id: Mapped[int] = mapped_column(ForeignKey("entities.id"), index=True)
    alias: Mapped[str] = mapped_column(String(512), index=True)
    alias_type: Mapped[str] = mapped_column(String(64), default="name")
    first_seen: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    last_seen: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)

    entity: Mapped[EntityRecord] = relationship(back_populates="aliases")


class ObservationRecord(Base):
    __tablename__ = "observations"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    source_name: Mapped[str] = mapped_column(String(255), index=True)
    source_type: Mapped[str] = mapped_column(String(64), index=True)
    source_tier: Mapped[str] = mapped_column(String(1), index=True)
    source_url: Mapped[str | None] = mapped_column(Text, nullable=True)
    published_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    observed_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), index=True)
    content_hash: Mapped[str] = mapped_column(String(64), unique=True, index=True)
    content_type: Mapped[str] = mapped_column(String(64), default="text")
    language: Mapped[str | None] = mapped_column(String(16), nullable=True)
    metadata_json: Mapped[dict[str, Any]] = mapped_column(JSON, default=dict)


class EvidenceRecord(Base):
    __tablename__ = "evidence"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    observation_id: Mapped[int] = mapped_column(ForeignKey("observations.id"), index=True)
    evidence_key: Mapped[str] = mapped_column(String(128), unique=True, index=True)
    sha256: Mapped[str] = mapped_column(String(64), index=True)
    storage_uri: Mapped[str] = mapped_column(Text)
    review_status: Mapped[str] = mapped_column(String(32), default="unreviewed")
    notes: Mapped[str | None] = mapped_column(Text, nullable=True)


class RelationshipRecord(Base):
    __tablename__ = "relationships"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    source_entity_id: Mapped[int] = mapped_column(ForeignKey("entities.id"), index=True)
    target_entity_id: Mapped[int] = mapped_column(ForeignKey("entities.id"), index=True)
    relationship_type: Mapped[str] = mapped_column(String(64), index=True)
    confidence: Mapped[float] = mapped_column(Float, default=1.0)
    first_seen: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    last_seen: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    review_status: Mapped[str] = mapped_column(String(32), default="unreviewed")
    evidence_ids: Mapped[list[int]] = mapped_column(JSON, default=list)


class IndicatorRecord(Base):
    __tablename__ = "indicators"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    scheme_entity_id: Mapped[int] = mapped_column(ForeignKey("entities.id"), index=True)
    indicator_type: Mapped[str] = mapped_column(String(128), index=True)
    severity: Mapped[str] = mapped_column(String(32), default="medium")
    status: Mapped[str] = mapped_column(String(32), default="active")
    confidence: Mapped[float] = mapped_column(Float, default=1.0)
    first_seen: Mapped[datetime] = mapped_column(DateTime(timezone=True), index=True)
    last_seen: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    evidence_ids: Mapped[list[int]] = mapped_column(JSON, default=list)


class RiskSnapshotRecord(Base):
    __tablename__ = "risk_snapshots"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    scheme_entity_id: Mapped[int] = mapped_column(ForeignKey("entities.id"), index=True)
    snapshot_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), index=True)
    risk_state: Mapped[str] = mapped_column(String(64), index=True)
    internal_score: Mapped[int] = mapped_column(Integer)
    active_indicator_count: Mapped[int] = mapped_column(Integer)
    explanation_json: Mapped[dict[str, Any]] = mapped_column(JSON, default=dict)


def build_engine(database_url: str = "sqlite+pysqlite:///:memory:"):
    return create_engine(database_url, future=True)


def create_schema(database_url: str = "sqlite+pysqlite:///:memory:"):
    engine = build_engine(database_url)
    Base.metadata.create_all(engine)
    return engine


def session_factory(database_url: str = "sqlite+pysqlite:///:memory:") -> sessionmaker[Session]:
    engine = create_schema(database_url)
    return sessionmaker(bind=engine, class_=Session, expire_on_commit=False)
