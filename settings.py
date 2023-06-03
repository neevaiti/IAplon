import os
import logging

from logging.config import dictConfig
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')

# Config logging
LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s"  
        },
        "standard": {
            "format": "%(asctime)s %(levelname)s %(message)s"
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "standard",
            "level": "DEBUG"
        },
        "console2": {
            "class": "logging.StreamHandler",
            "formatter": "standard",
            "level": "WARNING"  
        },
        "file": {
            "class": "logging.FileHandler",
            "level": "INFO",
            "filename": "Logs/infos.log",
            "mode": "w",
            "formatter": "standard"
        }
    },
    "loggers": {
        "bot": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": False
        },
        "discord": {
            "handlers": ["console2", "file"],
            "level": "INFO",
            "propagate": False
        }
    }
}