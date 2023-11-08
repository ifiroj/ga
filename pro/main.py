from fastapi import *
from mainApp.route import api

app = FastAPI()
app.include_router(api)

## change in change