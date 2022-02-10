from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated = "auto")

class Hash():
    def bcrypt(password: str):
        hashedPassword = pwd_cxt.hash(password)
        return hashedPassword

    def verify(user_password, request_password):
        return pwd_cxt.verify(request_password, user_password )
