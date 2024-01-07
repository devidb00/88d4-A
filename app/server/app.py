import logging
from fastapi import FastAPI
from server.config import settings
from server.database import MongoDB
from contextlib import asynccontextmanager
# routers
from server.routes.account import router as AccountRouter

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Database connection
    db_name = settings.mongodb_name
    db_username = settings.mongodb_username
    db_password = settings.mongodb_password

    try:
        app.mongodb_client = MongoDB(db_username, db_password)
        app.database = app.mongodb_client.connect(db_name)

        logging.info("Connected to the MongoDB database!")
    except Exception as e:
        print(e)

    yield
    print("Connection failed. Check DB credentials!")

app = FastAPI(lifespan=lifespan)

# routers path
app.include_router(AccountRouter, tags=['Account'], prefix="/api/account")

