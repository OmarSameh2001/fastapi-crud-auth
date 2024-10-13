from datetime import datetime, timedelta

from bson import ObjectId
from pydantic import BaseModel, field_validator, Field, computed_field
from config.db import conn

class Item(BaseModel):
    name: str = Field(..., pattern="^[a-zA-Z0-9 ]+$")
    description: str
    date_found: datetime
    date_lost: datetime
    date_claimed: datetime
    location_found: str
    location_claimed: str
    location_lost: str
    loser_id: str
    claimer_id: str
    founder_id: str
    status: str = Field(...)

    @field_validator("status")
    def check_status(cls, v):
        if v is None or v not in ["found", "claimed", "lost"]:
            raise ValueError("Status should be found or claimed or lost")
        return v
    @field_validator("loser_id")
    def check_loser_id_in_user(cls, v):
        if v is not None and v != "":
            if conn.user.find_one({"_id":ObjectId(v)}) is None:
                raise ValueError("Founder id should be valid user")
        return v

    @field_validator("claimer_id")
    def check_claimer_id_in_user(cls, v):
        if v is not None and v != "":
            if conn.user.find_one({"_id":ObjectId(v)}) is None:
                raise ValueError("Founder id should be valid user")
        return v

    @field_validator("founder_id")
    def check_founder_id_in_user(cls, v):
        if v is not None and v != "":
            if conn.user.find_one({"_id":ObjectId(v)}) is None:
                raise ValueError("Founder id should be valid user")
        return v

    # @computed_field
    # def claim_time(self) -> timedelta | None:
    #     if self.status == "claimed" and self.date_claimed and self.date_found:
    #         return self.date_claimed - self.date_found
    #     return None



