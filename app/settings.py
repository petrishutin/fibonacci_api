from pydantic import BaseSettings


class Config(BaseSettings):
    """Config of microservice"""
    LOG_LEVEL: str = 'INFO'

    class Config:
        case_sensitive = True
        env_file = '.env'


config = Config()
