import uvicorn
from fastapi import Depends, FastAPI
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from app.sample.entities.token import Token
from app.sample.entities.user import User
import app.sample.exceptions as exceptions
import app.sample.authentication as authentication
import app.sample.use_cases as use_cases

app = FastAPI()
security = HTTPBasic()


@app.post("/token", response_model=Token)
def login_for_access_token(credentials: HTTPBasicCredentials = Depends(security)):
    user = use_cases.get_user(credentials.username, credentials.password)
    if not user:
        raise exceptions.unauthenticated_user
    access_token = authentication.generate_access_token(credentials.username)
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/vehicles")
def get_own_vehicles(user: User = Depends(authentication.get_current_active_user)):
    return use_cases.get_vehicles(user.username)

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=80)
