from pydantic import BaseSettings


class Config(BaseSettings):
    """Config of microservice"""
    LOG_LEVEL: str = 'INFO'
    MAX_FIBONACCI: int = 1000
    REDIS_HOST: str = 'redis'
    REDIS_PORT: str = 6379
    REDIS_USER: str = None
    REDIS_PASSWORD: str = None

    class Config:
        case_sensitive = True
        env_file = '../.env'


config = Config()
