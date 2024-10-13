from datetime import datetime
from pydantic import BaseModel, field_validator, Field

class User(BaseModel):
    name: str
    username: str
    email: str
    password: str
    role: str = "user"
    created_at: datetime
class UserRegister(BaseModel):
    name: str
    username: str
    email: str = Field(...)
    password: str
class UserLogin(BaseModel):
    email: str = Field(...)
    password: str

    # @field_validator("username")
    # def username_unique(cls, v):
    #     if v in [user.username for user in cls.__class__.__dict__.get("objects", [])]:
    #         raise ValueError("Username already exists")
    #     return v
    #
    # @field_validator("email")
    # def email_unique(cls, v):
    #     if v in [user.email for user in cls.__class__.__dict__.get("objects", [])]:
    #         raise ValueError("Email already exists")
    #     return v

    class Config:
        arbitrary_types_allowed = True