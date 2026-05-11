from fastapi import Depends, APIRouter
from fastapi.responses import JSONResponse

router = APIRouter(prefix="/auth")

@router.post("/register")
async def register_user():
    return JSONResponse(content={"message": "User registered successfully"}, status_code=201)

@router.post("/login")
async def login_user():
    return JSONResponse(content={"message": "User logged in successfully"}, status_code=200)

@router.post("/logout")
async def logout_user():
    return JSONResponse(content={"message": "User logged out successfully"}, status_code=200)