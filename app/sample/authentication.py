import datetime
import os
import jwt
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from app.sample.entities.token_data import TokenData
import app.sample.exceptions as exceptions
from app.sample.entities.user import User
import app.sample.use_cases as use_cases

ALGORITHM = 'HS256'
SECRET = os.environ['SECRET']

def generate_access_token(username):
    expiration_time = datetime.datetime.now() + datetime.timedelta(minutes=10)
    data = {'usr': username, 'exp': expiration_time}
    encoded_jwt = jwt.encode(
        data,
        SECRET,
        algorithm=ALGORITHM,
    )
    return encoded_jwt

async def get_current_user(token: str = Depends(OAuth2PasswordBearer(tokenUrl="/token"))):
    try:
        payload = jwt.decode(token, SECRET, algorithms=[ALGORITHM])
        username: str = payload.get("usr")
        if username is None:
            raise exceptions.invalid_token
        token_data = TokenData(username=username)
    except jwt.InvalidTokenError:
        raise exceptions.invalid_token
    user = use_cases.get_user(username=token_data.username)
    if user is None:
        raise exceptions.user_not_found
    return user

async def get_current_active_user(current_user: User = Depends(get_current_user)):
    return current_user
