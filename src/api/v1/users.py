from typing import List
from fastapi import Depends, APIRouter, HTTPException
from src.services.users_service import UsersService
from src.orm.schemas.users import User, CreateUser, UpdateUser
from src.utils.CustomErrors import UserNotFoundError, UserExistError, UserIncorrectData

router = APIRouter(prefix="/users")

@router.get("/")
async def list_users(
        service: UsersService = Depends(UsersService)
) -> List[User]:
    return await service.list()

@router.get("/{user_id}")
async def get_user(
        user_id: int,
        service: UsersService = Depends(UsersService)
) -> User:
    try:
        return await service.get(user_id)
    except UserNotFoundError as e:
        raise HTTPException(status_code=404, detail={
            "error": "User not found",
            "traceback": e.__str__()
        })

@router.post("/")
async def create_user(
        user: CreateUser,
        service: UsersService = Depends(UsersService)
) -> User:
    try:
        return await service.create(user)
    except UserExistError as e:
        raise HTTPException(status_code=400, detail={
            "error": "User already exists",
            "traceback": e.__str__()
        })
    except UserIncorrectData as e:
        raise HTTPException(status_code=400, detail={
            "error": "Incorrect data",
            "traceback": e.__str__()
        })

@router.put("/{user_id}")
async def update_user(
        user_id: int,
        user: UpdateUser,
        service: UsersService = Depends(UsersService)
) -> User:
    try:
        return await service.update(user_id, user)
    except UserExistError as e:
        raise HTTPException(status_code=400, detail={
            "error": "User already exists",
            "traceback": e.__str__()
        })
    except UserIncorrectData as e:
        raise HTTPException(status_code=400, detail={
            "error": "Incorrect data",
            "traceback": e.__str__()
        })
    except UserNotFoundError as e:
        raise HTTPException(status_code=404, detail={
            "error": "User not found",
            "traceback": e.__str__()
        })

@router.delete("/{user_id}")
async def delete_user(
        user_id: int,
        service: UsersService = Depends(UsersService)
) -> User:
    try:
        return await service.delete(user_id)
    except UserNotFoundError as e:
        raise HTTPException(status_code=400, detail={
            "error": "User not found",
            "traceback": e.__str__()
        })
