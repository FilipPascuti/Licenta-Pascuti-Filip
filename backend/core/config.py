from typing import List

from pydantic import PostgresDsn, BaseSettings, AnyHttpUrl


class Settings(BaseSettings):
    API_STR: str = "/api"
    PROJECT_NAME: str = "licenta backend"

    SECRET_KEY: str = "c7b3ce1fd25e0dd17366611de0149aaa8ea3942660716aadc61510cae7dc3300"
    ALGORITHM: str = "HS256"

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    DATABASE_URI: str = "postgresql+psycopg2://postgres:postgres@127.0.0.1:5432/licenta"
    SHOW_DDL = False

    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = ["http://localhost:3000"]


settings = Settings()
