from passlib.context import CryptContext

# Create a password context to handle password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash:
         # Hash the password before storing it
    @staticmethod
    def bcrypt(password: str):
        return pwd_context.hash(password)
    
    @staticmethod
    def verify(hashed_password, plain_password):
        return pwd_context.verify(plain_password, hashed_password)
