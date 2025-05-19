from fastapi import HTTPException, status

from Specto.common.messages import UserMessages
from Specto.config import jwttoken
from Specto.config.db import user_collection
from Specto.config.hashing import Hash
from Specto.serializers.user_serializers import userResponseEntity


class UserService:
   

    async def sign_up(self, request):
        if request.password != request.confirm_password:
            raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST, detail=UserMessages.CONFIRM_PASSWORD.value
                )
    
        user_email = await user_collection.find_one({"email": request.email})

        if user_email:
            error_details = {"success": False, "message": UserMessages.EMAIL_ALREADY_REGISTERED.value, "data": {}}
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail=error_details
            )
        
        hashed_pass = Hash.bcrypt(request.password)
        user_object = dict(request)
        user_object["password"] = hashed_pass
        user_object["confirm_password"] = hashed_pass
        user = await user_collection.insert_one(user_object)
        user_detail = userResponseEntity(await user_collection.find_one({'_id': user.inserted_id}))
        return user_detail
    
    async def sign_in(self, request):
        user = await user_collection.find_one({"username":request.username})
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        
        if not Hash.verify(user["password"],request.password):
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        
        user_token_data = {
            "name": user["username"],
            "id": str(user["_id"]),
            "email": user["email"],
            "username": user["username"]
        }
        access_token = jwttoken.create_access_token(data=user_token_data)
        response_data = {"access_token": access_token, "token_type": "bearer"}
        return response_data
    
    async def create_user(google_user):
        user = await user_collection.find_one({"email": google_user["email"]})
        if not user:
            new_user = {
                "email": google_user["email"],
                "name": google_user.get("name"),
                "picture": google_user.get("picture"),
                "created_at": google_user.get("iat"),
            }
            await user_collection.insert_one(new_user)
            return new_user
        return user
    
    async def google_auth_service(self, request):
        pass