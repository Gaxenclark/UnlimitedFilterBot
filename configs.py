from os import environ
from logging import basicConfig, INFO, StreamHandler, getLogger, WARNING, Logger
from logging.handlers import RotatingFileHandler
from script import StartTxT, HelpTxT, AboutTxT

basicConfig( level=INFO, format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s", datefmt='%d-%b-%y %H:%M:%S', handlers=[ RotatingFileHandler("filtersbot.txt", maxBytes=50000000, backupCount=10), StreamHandler() ] )

getLogger("pyrogram").setLevel(WARNING)

def LOGGER(name: str) -> Logger:
    return getLogger(name)

if bool(environ.get("WEBHOOK", True)):

    try:
        API_ID = int(environ.get("API_ID", 25242804))
    except Exception as e:
        print(f"API_ID Invalid: \n\nLogs: {e}")

    try:
        API_HASH = environ.get("API_HASH", "bdc317842f60220121ded0a2fcdc0727")
    except Exception as e:
        print(f"API_HASH Invalid: \n\nLogs: {e}")

    try:
        BOT_TOKEN = environ.get("BOT_TOKEN", "6212399137:AAG59qqOLn306rydBPF9pR8w7qeEX4UozgI")
    except Exception as e:
        print(f"BOT_TOKEN Invalid: \n\nLogs: {e}")

    try:
        DATABASE_URI = environ.get("DATABASE_URI", "mongodb+srv://gdc846017:blackpanther00@cluster0.zpakafu.mongodb.net/?retryWrites=true&w=majority")
    except Exception as e:
        print(f"DATABASE_URI Invalid: \n\nLogs: {e}")

    try:
        DATABASE_NAME = environ.get("DATABASE_NAME", "Muhammed")
    except Exception as e:
        print(f"DATABASE_NAME Invalid: \n\nLogs: {e}")

    try:
        ADMINS = set(str(x) for x in environ.get("ADMINS", "6046028054").split())
    except Exception as e:
        print(f"ADMINS Invalid: \n\nLogs: {e}")

    # OPTIONAL - To set alternate BOT COMMANDS

    ADD_FILTER_CMD = environ.get("ADD_FILTER_CMD", "add")

    DELETE_FILTER_CMD = environ.get("DELETE_FILTER_CMD", "del")

    DELETE_ALL_CMD = environ.get("DELETE_ALL_CMD", "delall")

    CONNECT_COMMAND = environ.get("CONNECT_CMD", "connect")

    DISCONNECT_COMMAND = environ.get("DISCONNECT_CMD", "disconnect")

    BOT_PICS = (environ.get('BOT_PICS', "motech")).split()

    FORCE_SUB = environ.get("UPDATE_CHANNEL", "t.me/TooAdultsVideos")

    SUPPORT_CHAT = environ.get("SUPPORT_CHAT", "TooAdultsVideos")

    START_TXT = environ.get("START_TXT", StartTxT)

    HELP_TXT = environ.get("HELP_MESSAGE", HelpTxT)

    ABOUT_TXT = environ.get("ABOUT_MESSAGE", AboutTxT)

    AUTO_DELETE = bool(environ.get("AUTO_DELETE", True))

    AUTO_DELETE_SECOND = int(environ.get("AUTO_DELETE_SECOND", 30))

    PORT = environ.get('PORT', '8080')

else:

    print("WEBHOOK is Disabled 😴")
