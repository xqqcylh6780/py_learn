# -*- coding: utf-8 -*-
"""13 logging.config.dictConfig：工程级集中配置。"""
import logging
import logging.config

CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "brief": {"format": "%(levelname)s %(name)s: %(message)s"},
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "brief",
            "stream": "ext://sys.stdout",
        },
    },
    "loggers": {
        "app": {
            "level": "DEBUG",
            "handlers": ["console"],
            "propagate": False,
        },
    },
}

logging.config.dictConfig(CONFIG)
logger = logging.getLogger("app.service")
logger.debug("被 console 的 INFO 级别过滤")
logger.info("dictConfig 配置成功")

print("\ndisable_existing_loggers=False 通常更安全；设 True 可能意外禁用第三方库 logger。")
