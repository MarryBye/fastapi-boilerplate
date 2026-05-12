from fastapi import FastAPI
from fastapi.middleware import cors

from src.api.v1 import router as v1

from src.orm.config import engine
from src.orm.entities import create_tables

app = FastAPI()

@app.on_event("startup")
async def on_startup():
    await create_tables(engine)

app.include_router(v1)

app.add_middleware(
    cors.CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)