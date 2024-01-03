from fastapi import FastAPI
from server.config import settings
from server.database import MongoDB

# routers
from server.routes.account import router as AccountRouter
app = FastAPI()

# routers path (include)
app.include_router(AccountRouter, tags=['User'], prefix="/api/user")

@app.on_event("startup")
def startup_db_client():
    # Database connection
    db_name = settings.model_config.get('MONGODB_NAME')
    db_username = settings.model_config.get('MONGODB_USERNAME')
    db_password = settings.model_config.get('MONGODB_PASSWORD')

    try:
        app.mongodb_client = MongoDB(db_username, db_password)
        app.database = app.mongodb_client.connect(db_name)
        print("Connected to the MongoDB database!")
    except:
        print("Connection failed. Check DB credentials!")

@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()