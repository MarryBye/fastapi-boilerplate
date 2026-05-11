from src.alchemy.entities.base import metadata
from src.alchemy.entities.users import users

async def create_tables(engine):
    async with engine.begin() as conn:
        await conn.run_sync(metadata.create_all)