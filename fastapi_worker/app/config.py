from pydantic_settings import BaseSettings


class Config(BaseSettings):
    debug: str
    api_prefix: str
    database_url: str


settings = Config()
