from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import create_async_engine,async_sessionmaker
from pathlib import Path
from pydantic_settings import BaseSettings,SettingsConfigDict

BASE_DIR=Path(__file__).resolve().parent.parent

class Settings(BaseSettings):
    DATABASE_URL:str 
    REDIS_HOST:str
    REDIS_PORT:int
    model_config=SettingsConfigDict(env_file=BASE_DIR/'.env')

settings = Settings()

engine = create_async_engine(
    settings.DATABASE_URL,
    pool_size=10,
    max_overflow=5,
    pool_pre_ping=True,
    pool_timeout=30
)

AsyncLocalSession = async_sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False 
)

class Base(DeclarativeBase):
    pass 

async def getdb():
    async with AsyncLocalSession() as db:
        yield db 