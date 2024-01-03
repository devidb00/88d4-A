import os
from fastapi import FastAPI
from dotenv import load_dotenv
from server.database import MongoDB

# routers
from server.routes.account import router as AccountRouter

load_dotenv()

app = FastAPI()

# routers path (include)
app.include_router(AccountRouter, tags=['User'], prefix="/api/user")

@app.on_event("startup")
def startup_db_client():
    # Database connection
    db_name = os.getenv('MONGODB_NAME')
    db_username = os.getenv('MONGODB_USERNAME')
    db_password = os.getenv('MONGODB_PASSWORD')

    try:
        app.mongodb_client = MongoDB(db_username, db_password)
        app.database = app.mongodb_client.connect(db_name)
        print("Connected to the MongoDB database!")
    except:
        print("Connection failed. Check DB credentials!")

@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()