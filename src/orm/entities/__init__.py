from src.orm.entities.base import metadata
from src.orm.entities.users import users

async def create_tables(engine):
    async with engine.begin() as conn:
        await conn.run_sync(metadata.create_all)