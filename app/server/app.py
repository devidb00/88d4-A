import os
from dotenv import load_dotenv

from fastapi import FastAPI
from server.database import MongoDB

# routers
from server.routes.user import router as UserRouter

app = FastAPI()

load_dotenv()

# Database connection
db_username = os.getenv('MONGODB_USERNAME')
db_password = os.getenv('MONGODB_PASSWORD')
database = MongoDB(db_username, db_password).connect()

# routers path (include)
app.include_router(UserRouter, tags=['User'], prefix="/user")

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}