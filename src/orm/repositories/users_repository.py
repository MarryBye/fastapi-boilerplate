from typing import List
from fastapi import Depends
from sqlalchemy import select, insert, update, delete, func
from sqlalchemy.ext.asyncio import AsyncSession
from src.orm.entities.users import users
from src.orm.config import get_session
from src.orm.schemas.users import User, UpdateUser, CreateUser

class UsersRepository:
    def __init__(self, session: AsyncSession = Depends(get_session)):
        self.session = session

    async def create(self, user: CreateUser) -> User:
        print(user.model_dump())
        payload = await self.session.execute(
            insert(users)
            .values(**user.model_dump())
            .returning(users)
        )

        await self.session.commit()

        return User(**payload.mappings().one())

    async def list(self, limit: int = 10, offset: int = 0) -> List[User]:
        payload = await self.session.execute(
            select(users)
            .limit(limit)
            .offset(offset)
        )

        return [User(**payload) for payload in payload.mappings().all()]

    async def get(self, pk: int) -> User:
        payload = await self.session.execute(
            select(users)
            .where(users.c.id == pk)
        )

        return User(**payload.mappings().one())

    async def update(self, pk: int, user: UpdateUser) -> User:
        payload = await self.session.execute(
            update(users)
            .where(users.c.id == pk)
            .values(**user.model_dump(exclude_unset=True))
            .returning(users)
        )

        await self.session.commit()

        return User(**payload.mappings().one())

    async def delete(self, pk: int) -> User:
        payload = await self.session.execute(
            delete(users)
            .where(users.c.id == pk)
            .returning(users)
        )

        await self.session.commit()

        return User(**payload.mappings().one())
