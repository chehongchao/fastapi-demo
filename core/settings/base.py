# 基础配置

class Config:
    DEBUG = False
    PORT = 8000
    SECRET_KEY = "your-secret-key"
    DATABASE_URL = ""  # 这只是一个默认值，可以在子类中覆盖
