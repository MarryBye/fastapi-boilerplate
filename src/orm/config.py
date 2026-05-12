from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from config import Config

DATABASE_URL = f"postgresql+asyncpg://{Config.Database.USER}:{Config.Database.PASSWORD}@{Config.Database.HOST}:{Config.Database.PORT}/{Config.Database.NAME}"

engine = create_async_engine(DATABASE_URL, echo=True)
SessionFactory = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with SessionFactory() as session:
        yield session