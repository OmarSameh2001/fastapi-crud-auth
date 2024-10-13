def userEntity(item) -> dict:
    return {
        "id":str(item["_id"]),
        "name":item["name"],
        "email":item["email"],
        "username":item["username"],
        "role":item["role"],
        "created_at":item["created_at"]
    }

def usersEntity(entity) -> list:
    return [userEntity(item) for item in entity]