from core.settings.base import Config


# 开发环境配置
class DevConfig(Config):
    DEBUG = True
    DATABASE_URL = "mysql://root:root@localhost:3306/fastapi-demo"
    REDIS_URL = "redis://localhost:6379/0"
