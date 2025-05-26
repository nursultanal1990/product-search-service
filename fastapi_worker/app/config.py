from pydantic_settings import BaseSettings


class Config(BaseSettings):
    database_url: str
    elasticsearch_host: str
    kafka_bootstrap_servers: str
    app_name: str


settings = Config()
