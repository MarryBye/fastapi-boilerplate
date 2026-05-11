import dotenv
import os

is_loaded = dotenv.load_dotenv("./config/.env.dev")

if not is_loaded:
    raise Exception("Failed to load environment variables")

class Config:
    class Database:
        HOST = os.getenv("DATABASE_HOST")
        USER = os.getenv("DATABASE_USER")
        PASSWORD = os.getenv("DATABASE_PASSWORD")
        NAME = os.getenv("DATABASE_NAME")
        PORT = os.getenv("DATABASE_PORT")

    class JWT:
        SECRET = os.getenv("JWT_SECRET")
        ALGORITHM = os.getenv("JWT_ALGORITHM")
        EXPIRATION_MINUTES = os.getenv("JWT_EXPIRATION_MINUTES")