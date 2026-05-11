from sqlalchemy import Table, Column, Integer, String, DateTime, func, Enum
from src.alchemy.entities.base import metadata
from src.alchemy.types import Roles, LowerString, EmailString

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String(32), nullable=False),
    Column("login", LowerString(32), unique=True, nullable=False),
    Column("hashed_password", String(256), nullable=False),
    Column("role", Enum(Roles), nullable=False, default=Roles.USER),
    Column("email", EmailString(256), nullable=False, unique=True),
    Column("created_at", DateTime, nullable=False, default=func.now()),
    Column("updated_at", DateTime, nullable=False, default=func.now(), onupdate=func.now())
)