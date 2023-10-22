import os

from core.settings.dev import DevConfig
from core.settings.prod import ProdConfig

ENV = os.environ.get("ENV", "development")  # 默认为开发环境

if ENV == "development":
    config = DevConfig
elif ENV == "production":
    config = ProdConfig
else:
    raise ValueError(f"Invalid ENV value: {ENV}")
