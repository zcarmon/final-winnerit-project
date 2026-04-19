import os
from dotenv import load_dotenv

#Load the value of the x-api-key from .env
load_dotenv()
X_API_KEY_FIELD = "x-api-key"

#this is the key
X_API_KEY_VALUE = os.getenv("X_API_KEY")

STATUS_CODE_OK = 200

BASE_URL = "https://reqres.in/api/"

USERS_URL = "users/"

HEADER = {X_API_KEY_FIELD: X_API_KEY_VALUE}