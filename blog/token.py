from datetime import datetime, timedelta
from jose import JWTError, jwt
from fastapi import HTTPException,status
from . import schemas


SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_token(token: str,credentials_exception):
    try:
        # Decode the JWT token and return the payload
       ''' payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")'''
       payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
       email:str = payload.get("sub")
       if email is None:
           raise credentials_exception
       token_data =schemas.TokenData(email=email)
    except JWTError:
        raise credentials_exception
