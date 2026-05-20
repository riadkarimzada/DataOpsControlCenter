from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "DataOps Control Center API"
    environment: str = "development"
    database_url: str = "postgresql://dataops_user:dataops_password@localhost:5432/dataops_db"

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()