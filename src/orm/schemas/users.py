import datetime
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, EmailStr
from src.orm.types import Roles


class BaseUser(BaseModel):
    username: str
    login: str
    hashed_password: str
    role: Roles
    email: EmailStr

class User(BaseUser):
    id: int
    created_at: datetime
    updated_at: datetime

class CreateUser(BaseUser):
    pass

class UpdateUser(BaseModel):
    username: Optional[str] = None
    login: Optional[str] = None
    hashed_password: Optional[str] = None
    role: Optional[Roles] = None
    email: Optional[EmailStr] = None

class RegisterUser(BaseModel):
    username: str
    login: str
    hashed_password: str
    email: EmailStr

class LoginUser(BaseModel):
    login: str
    hashed_password: str