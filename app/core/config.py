import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings
load_dotenv()

class Settings(BaseSettings):
    DATABASE_URL: str

    class Config:
        env_file = ".env"

settings = Settings(
    DATABASE_URL=os.environ.get('DATABASE_URL')
)
