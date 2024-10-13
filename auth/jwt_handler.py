from datetime import datetime, timedelta
from jose import JWTError, jwt

SECRET_KEY = "fast-777" # should be kept secret (.env)
ALGORITHM = "HS256" # standard algorithm for encoding
ACCESS_TOKEN_EXPIRE_MINUTES = 60 # default value

# Create a token
def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now() + expires_delta
    else:
        expire = datetime.now() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Decode and verify token
def decode_access_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None
