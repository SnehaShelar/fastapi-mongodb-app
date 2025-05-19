from bson import ObjectId
from fastapi import APIRouter, Depends, HTTPException, Request, status
from fastapi.responses import RedirectResponse

from Specto.common.messages import UserMessages
from Specto.common.response import ResponseHandler
from Specto.config import jwttoken
from Specto.config.db import (client, user_collection,
                              user_device_token_collection)
from Specto.config.hashing import Hash
from Specto.config.oauth import get_current_user, get_google_user, oauth
from Specto.decorators.transaction_decorator import with_transaction
from Specto.schemas.user_schema import (AccountSettingsSchema, LoginSchema,
                                 UserDeviceTokens, UserSchema)
from Specto.serializers.user_serializers import userResponseEntity
from Specto.services import UserService

router = APIRouter(
    prefix='/specto',
    tags=['Authentication']
)

@with_transaction
@router.post('/sign-up/', status_code=status.HTTP_201_CREATED)
async def register(request:UserSchema):
    user_response = await UserService().sign_up(request)
    return ResponseHandler.success(message=UserMessages.USER_REGISTERED_SUCCESSFULLY.value, data=user_response)

@with_transaction
@router.post('/sign-in/')
async def login(request: LoginSchema):
    user_response = await UserService().sign_in(request)
    return ResponseHandler.success(message=UserMessages.USER_LOGGED_SUCCESSFULLY.value, data=user_response)

@router.post('/sign-out/')
async def logout():
    return ResponseHandler.success(message=UserMessages.USER_LOGGED_OUT_SUCCESSFULLY.value, data={})

async def get_or_create_user(google_user: dict):
    user = await UserService().create_user(google_user)
    return user
