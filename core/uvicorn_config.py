import logging

from logger_config import logger


class InterceptHandler(logging.Handler):
    def emit(self, record):
        # 获取对应的 Loguru 级别
        logger_opt = logger.opt(depth=10, exception=record.exc_info)
        logger_opt.log(record.levelno, record.getMessage())


logging.getLogger("uvicorn").handlers = [InterceptHandler()]
logging.getLogger("uvicorn.access").handlers = [InterceptHandler()]
