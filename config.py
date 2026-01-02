import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8387440827:AAFuE8cD6GS7ShNwovdRCGLc49x59gD1Ufo")  # Ensure correct key name
    API_ID = int(os.environ.get("API_ID", "22447622"))  # Added key name and default value
    API_HASH = os.environ.get("API_HASH", "543b62d58d3e723e766ba57a984ab65d")  # Added key name for consistency

    AUTH_USER = os.environ.get("AUTH_USERS", "777756062").split(',')
    AUTH_USERS = [int(user_id) for user_id in AUTH_USER]  # Ensuring list of integers

    HOST = os.environ.get("HOST", "http://master-api-v3.vercel.app")  # Keeping HOST configurable
    CREDIT = os.environ.get("CREDIT", "𝙎𝘼𝙄𝙉𝙄 𝘽𝙊𝙏𝙎")  # Making CREDIT an environment variable for flexibility


