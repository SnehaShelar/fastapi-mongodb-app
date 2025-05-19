import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings
import os
from dotenv import load_dotenv

# Check if the file exists
env_path = os.path.join(os.path.dirname(__file__), ".env")

if os.path.exists(env_path):
    print(f"Found .env file at: {env_path}")
    load_dotenv(env_path)
else:
    print(".env file not found!")

class Settings(BaseSettings):
    MONGO_INITDB_ROOT_USERNAME: str = os.getenv("MONGO_INITDB_ROOT_USERNAME")
    MONGO_INITDB_ROOT_PASSWORD: str = os.getenv("MONGO_INITDB_ROOT_PASSWORD")
    MONGO_INITDB_DATABASE: str = os.getenv("MONGO_INITDB_DATABASE")

    MONGO_URI: str = os.getenv("MONGO_URI")
    DATABASE_NAME: str = os.getenv("DATABASE_NAME")

    SECRET_KEY: str = os.getenv("SECRET_KEY")
    ALGORITHM: str = os.getenv("ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))

    CELERY_BROKER_URL: str = os.getenv("CELERY_BROKER_URL")
    CELERY_RESULT_BACKEND: str = os.getenv("CELERY_RESULT_BACKEND")
    
    GOOGLE_APPLICATION_CREDENTIALS: str = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
    FRONTEND_URL: str = os.getenv("FRONTEND_URL")

    GOOGLE_CLIENT_ID: str = os.getenv("GOOGLE_CLIENT_ID")
    GOOGLE_CLIENT_SECRET: str = os.getenv("GOOGLE_CLIENT_SECRET")
    GOOGLE_ACCESS_TOKEN_URI: str = os.getenv("GOOGLE_ACCESS_TOKEN_URI")
    GOOGLE_AUTHORIZE_URI: str = os.getenv("GOOGLE_AUTHORIZE_URI")

app_settings = Settings()
