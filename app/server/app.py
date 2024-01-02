from fastapi import FastAPI

# routers
from server.routes.account import router as AccountRouter

app = FastAPI()

# routers path (include)
app.include_router(AccountRouter, tags=['User'], prefix="/api/user")

@app.get("/", tags=["Root"])
def root():
    return {"message": "Welcome to this fantastic app!"}