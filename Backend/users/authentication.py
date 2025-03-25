import jwt
import datetime
from django.conf import settings

# SECRET_KEY = settings.SECRET_KEY
SECRET_KEY = 'django-insecure-h5-((v%l!xfk#ahu5v-w3fbj7*2%3xz!6v&xm04@hth-49dbu_'

class JWTHandler:
    @staticmethod
    def generate_tokens(user_id):
        access_token_exp = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        refresh_token_exp = datetime.datetime.utcnow() + datetime.timedelta(days=7)

        access_token = jwt.encode(
            {"user_id": user_id, "exp": access_token_exp},
            SECRET_KEY,
            algorithm="HS256"
        )

        refresh_token = jwt.encode(
            {"user_id": user_id, "exp": refresh_token_exp},
            SECRET_KEY,
            algorithm="HS256"
        )

        return access_token, refresh_token

    @staticmethod
    def decode_token(token):
        try:
            decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            return decoded
        except jwt.ExpiredSignatureError:
            return None
        except jwt.InvalidTokenError:
            return None
        
    @staticmethod
    def get_user_id_from_token(token):
        decoded = JWTHandler.decode_token(token)
        return decoded["user_id"] if decoded else None

       