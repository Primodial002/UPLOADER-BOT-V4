import os

import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)

class Config(object):
    
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5256191217:AAEmPSbsZXnG6-TtKMNpYcbHOW5HzvNe47A")
    
    API_ID = int(os.environ.get("API_ID", "11883248"))
    
    API_HASH = os.environ.get("API_HASH", "ed7c6fe18f8120bdd059a55d509e38e9")
    
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    
    MAX_FILE_SIZE = 2097152000
    
    TG_MAX_FILE_SIZE = 2097152000
    
    FREE_USER_MAX_FILE_SIZE = 2097152000
    
    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))
    
    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "")
    
    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")
    
    OUO_IO_API_KEY = ""
    
    MAX_MESSAGE_LENGTH = 4096
    
    PROCESS_MAX_TIMEOUT = 0
    
    DEF_WATER_MARK_FILE = "@AdultFilmsPlus"
    
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://hkwzmlx:hkwzmlx@cluster0.hzo64.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0     ")
    
    SESSION_NAME = os.environ.get("SESSION_NAME", "UploadLinkToFileBot")
    
    LOG_CHANNEL = -1001636559929
    
    LOGGER = logging

    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "")
    
    OWNER_ID = int(os.environ.get("OWNER_ID", "2090127712"))
    
    TG_MIN_FILE_SIZE = 2097152000
    
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Catub010_bot")
                                  
