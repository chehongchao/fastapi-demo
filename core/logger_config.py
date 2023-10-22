# logger.py
from loguru import logger

# 配置日志输出
# 使用 "logs/{time:YYYY-MM}/" 来为每个月创建一个文件夹
# 使用 rotation="1 day" 来按日分割日志
logger.add("logs/{time:YYYY-MM}/{time:YYYY-MM-DD}.log", rotation="1 day", level="INFO")
