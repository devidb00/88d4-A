import logging
from fastapi import FastAPI
from server.config import settings
from server.database import mongodb_db
from contextlib import asynccontextmanager
# routers
from server.routes.account import router as AccountRouter
from server.routes.account import router as OrderRouter

@asynccontextmanager
async def lifespan(app: FastAPI):
    db_name = settings.mongodb_name
    try:
        mongodb_db.connect_db(db_name)
    except Exception as e:
        logging.error(e)
        
    yield
    mongodb_db.disconnect()

app = FastAPI(lifespan=lifespan)

# routers path
app.include_router(AccountRouter, tags=['Account'], prefix="/api/account")
app.include_router(OrderRouter, tags=['Order'], prefix="/api/order")


