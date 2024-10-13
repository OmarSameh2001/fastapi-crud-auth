from fastapi import FastAPI
from routes.user import user
from routes.item import item
from routes.auth_route import auth
app = FastAPI()
app.include_router(user)
app.include_router(item)
app.include_router(auth)
