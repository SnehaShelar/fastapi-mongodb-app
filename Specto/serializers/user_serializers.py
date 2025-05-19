def userEntity(user) -> dict:
    return {
        "id": str(user["_id"]),
        "username": user["username"],
        "email": user["email"],
        "password": user["password"],
        "confirm_password": user["confirm_password"]
    }

def userResponseEntity(user) -> dict:
    return {
        "id": str(user["_id"]),
        "username": user["username"],
        "email": user["email"],
        "created_at": user["created_at"],
        "updated_at": user["updated_at"]
    }
