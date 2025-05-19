from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class UserSchema(BaseModel):
    username: str
    email: str
    password: str
    confirm_password: str
    created_at: datetime | None = None
    updated_at: datetime | None = None

class LoginSchema(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None
    user_id: Optional[str] = None

class AccountSettingsSchema(BaseModel):
    username: str
    email: str
    name: str
    notificationToggle: bool
    deviceToken: str

class UserDeviceTokens(BaseModel):
    user_id: str
    fcm_device_token: str
    allowed_notification: bool = False