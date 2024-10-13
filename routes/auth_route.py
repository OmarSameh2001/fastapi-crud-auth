from datetime import datetime
from fastapi import APIRouter, HTTPException, status
from auth.hash_handler import hash_password, verify_password
from auth.jwt_handler import create_access_token
from config.db import conn
from models.user import UserLogin, UserRegister, User
auth = APIRouter()
# Authenticate user and create token
@auth.post("/login")
def login(user: UserLogin):
    if user.email is None or user.password is None:
        raise HTTPException(status_code=400, detail="Bad Request")
    user_data = conn.user.find_one({"email": user.email})
    if not user_data or not verify_password(user.password, user_data["password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
        )
    access_token = create_access_token(data={"sub": user.email, "role": user_data.role})
    return {"access_token": access_token, "token_type": "bearer"}
@auth.post("/register")
def register(user: UserRegister):
    # Check for existing user by email
    existing_user = conn.user.find_one({"email": user.email})
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    # Check for existing user by username
    existing_username = conn.user.find_one({"username": user.username})
    if existing_username:
        raise HTTPException(status_code=400, detail="Username already taken")

    # Hash the password and register the user
    hashed_password = hash_password(user.password)
    user.password = hashed_password
    new = User(name=user.name, username=user.username, email=user.email, password=hashed_password,
               role="user", created_at=datetime.now())
    conn.user.insert_one(dict(new))
    access_token = create_access_token(data={"sub": new.email, "role": new.role})
    return {"message": "User registered successfully!", "access_token": access_token, "token_type": "bearer"}