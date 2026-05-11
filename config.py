import os

class Config:
    class Database:
        HOST = os.getenv("PG_HOST")
        USER = os.getenv("POSTGRES_USER")
        PASSWORD = os.getenv("POSTGRES_PASSWORD")
        NAME = os.getenv("POSTGRES_DB")
        PORT = os.getenv("PG_PORT")

    class JWT:
        SECRET = os.getenv("JWT_SECRET")
        ALGORITHM = os.getenv("JWT_ALGORITHM")
        EXPIRATION_MINUTES = os.getenv("JWT_EXPIRATION_MINUTES")