from typing import List
from fastapi import Depends
from sqlalchemy.exc import IntegrityError, NoResultFound
from src.orm.schemas.users import User, UpdateUser, CreateUser, LoginUser, RegisterUser
from src.orm.repositories.users_repository import UsersRepository
from src.utils.CustomErrors import UserNotFoundError, UserExistError, UserIncorrectData

class UsersService:
    def __init__(self, users_repository: UsersRepository = Depends(UsersRepository)):
        self.users_repository = users_repository

    async def list(self) -> List[User]:
        return await self.users_repository.list()

    async def get(self, user_id: int) -> User:
        try:
            return await self.users_repository.get(user_id)
        except NoResultFound as e:
            raise UserNotFoundError(e)

    async def create(self, user: CreateUser) -> User:
        try:
            return await self.users_repository.create(user)
        except IntegrityError as e:
            await self.users_repository.session.rollback()

            orig = str(e.orig)

            if "duplicate key value violates unique constraint" in orig:
                raise UserExistError(e)
        except Exception as e:
            raise UserIncorrectData(e)

    async def update(self, user_id: int, user: UpdateUser) -> User:
        try:
            return await self.users_repository.update(user_id, user)
        except IntegrityError as e:
            await self.users_repository.session.rollback()

            orig = str(e.orig)

            if "duplicate key value violates unique constraint" in orig:
                raise UserExistError(e)
        except NoResultFound as e:
            raise UserNotFoundError(e)
        except Exception as e:
            raise UserIncorrectData(e)

    async def delete(self, user_id: int) -> User:
        try:
            return await self.users_repository.delete(user_id)
        except NoResultFound as e:
            raise UserNotFoundError(e)