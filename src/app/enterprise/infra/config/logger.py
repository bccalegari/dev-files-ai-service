import os
import sys
from datetime import datetime

from loguru import logger


class Logger:
    _instance = None
    _logger: logger = None
    _binds = {}

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._logger = logger
            cls._instance.__configure_logging()
        return cls._instance

    def __configure_logging(self):
        log_dir = "../logs"
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        self._setup_logger()

    def _setup_logger(self):
        self._logger.remove()
        self._logger = self._logger.bind(trace_id="N/A")

        format_string = "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level}</level> | Trace ID: <magenta>{extra[trace_id]}</magenta> | <cyan>{name}</cyan> | <level>{message}</level>"

        self._logger.add(sys.stdout, format=format_string, level="INFO", colorize=True, enqueue=True)

        log_filename = f"../logs/app_{datetime.now().strftime('%Y-%m-%d')}.log"
        self._logger.add(log_filename,
                          format=format_string,
                          level="INFO",
                          rotation="10 MB",
                          retention="10 days",
                          compression="zip",
                          enqueue=True)

    def info(self, message: str):
        self._logger.opt(depth=1).info(message)

    def error(self, message: str):
        self._logger.opt(depth=1).error(message)

    def bind(self, **kwargs):
        self._binds.update(kwargs)
        self._logger = self._logger.bind(**self._binds)

    def unbind(self, *args):
        for key in args:
            if key in self._binds:
                self._binds[key] = "N/A"
        self._logger = self._logger.bind(**self._binds)
