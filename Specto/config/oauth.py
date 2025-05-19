from fastapi import Depends,HTTPException
from Specto.config.jwttoken import verify_token
from fastapi.security import OAuth2PasswordBearer
from authlib.integrations.starlette_client import OAuth

from fastapi import Request, status
from Specto.settings import app_settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="sign-in")

oauth = OAuth()
oauth.register(
    name="google",
    client_id=app_settings.GOOGLE_CLIENT_ID,
    client_secret=app_settings.GOOGLE_CLIENT_SECRET,
    server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",
    client_kwargs={"scope": "openid email profile"},
)

async def get_google_user(request: Request):
    token = await oauth.google.authorize_access_token(request)
    print("OAuth Token Response:", token)
    return token

def get_current_user(token: str = Depends(oauth2_scheme)):
    
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    return verify_token(token,credentials_exception)



