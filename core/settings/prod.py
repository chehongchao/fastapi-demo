from core.settings.base import Config


# 生产环境配置
class ProdConfig(Config):
    DATABASE_URL = "postgresql://user:password@prod-db-server/dbname"
    REDIS_URL = "redis://prod-redis-server:6379/0"
