import os
from dotenv import load_dotenv


class Settings:
    def __init__(self):
        self.venmo_token = os.getenv("VENMO_TOKEN")


# also look at .env file for settings
load_dotenv(".env")

settings = Settings()
