import os
import logging
from logging.handlers import RotatingFileHandler
from logging.config import dictConfig
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')

# Obtenez le chemin absolu du fichier settings.py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOGS_DIR = os.path.join(BASE_DIR, 'Logs')

# Créez le répertoire Logs s'il n'existe pas
if not os.path.exists(LOGS_DIR):
    os.makedirs(LOGS_DIR)

# Format de date pour le nom du fichier de log
log_date_format = "%Y-%m-%d"

# Config logging
LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s"
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "verbose",
            "level": "DEBUG"
        },
        "file": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "DEBUG",
            "formatter": "verbose",
            "filename": os.path.join(LOGS_DIR, "infos.log"),
            "mode": "a",
            "maxBytes": 10485760,  # 10 MB
            "backupCount": 7
        }
    },
    "loggers": {
        "bot": {
            "handlers": ["console", "file"],
            "level": "DEBUG"
        },
        "discord": {
            "handlers": ["console", "file"],
            "level": "DEBUG"
        }
    }
}

# Ajoutez la date au nom du fichier de log
log_filename = f"infos_{datetime.now().strftime(log_date_format)}.log"
LOGGING_CONFIG['handlers']['file']['filename'] = os.path.join(LOGS_DIR, log_filename)

dictConfig(LOGGING_CONFIG)

logger = logging.getLogger("bot")
