from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "88d4-A"
    items_per_user: int = 50
    admin_email: str = "tarikidb.dev@gmail.com"
    model_config = SettingsConfigDict(env_file=".env", extra='allow', env_file_encoding='utf-8')

settings = Settings()