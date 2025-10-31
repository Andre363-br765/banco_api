from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # Banco de dados
    database_url: str = "sqlite:///./database.db"

    # Ambiente
    environment: str = "development"

    # JWT
    secret_key: str = "defaultsecret"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 60  # 1 hora


settings = Settings()
