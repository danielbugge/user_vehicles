from fastapi import HTTPException

invalid_token = HTTPException(
    status_code=401,
    detail="Invalid Token"
)

user_not_found = HTTPException(
    status_code=404,
    detail="User not found"
)

unauthenticated_user = HTTPException(
    status_code=401,
    detail="Incorrect username or password",
)
