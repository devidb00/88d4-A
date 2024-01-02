import os
from dotenv import load_dotenv

from fastapi import FastAPI
from server.database import MongoDB

# routers
from server.routes.account import router as AccountRouter

app = FastAPI()

load_dotenv()

# Database connection
db_name = os.getenv('MONGODB_NAME')
db_username = os.getenv('MONGODB_USERNAME')
db_password = os.getenv('MONGODB_PASSWORD')
database = MongoDB(db_username, db_password).connect(db_name)

# routers path (include)
app.include_router(AccountRouter, tags=['User'], prefix="/user")

@app.get("/", tags=["Root"])
def root():
    return {"message": "Welcome to this fantastic app!"}