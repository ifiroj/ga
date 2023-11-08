import os
from dotenv import load_dotenv

from fastapi import APIRouter

api = APIRouter()
load_dotenv()

@api.get("/mode")
def mode():
    return os.environ.get("MODE")

@api.get("/{string}")
def returnString(string:str):
    result = f"{string[::-1]}"
    return result