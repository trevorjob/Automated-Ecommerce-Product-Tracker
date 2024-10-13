from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


def create_jwt(user: User):  # type: ignore
    refresh = RefreshToken.for_user(user)
    tokens = {"refresh_token": str(refresh), "access_token": str(refresh.access_token)}
    return tokens
