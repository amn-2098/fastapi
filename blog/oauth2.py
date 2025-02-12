from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from . import token, schemas

# OAuth2PasswordBearer automatically fetches the token from the "Authorization" header
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(data: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    # Decode the token and get the payload (user info)
    return  token.verify_token(data, credentials_exception)
    # return schemas.TokenData(email=payload.get("sub"))

    
        # Decode the token and get the payload (user info)
       



''' user = schemas.TokenData(email=payload.get("sub"))
        if user is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
        return user
    except Exception:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")'''

