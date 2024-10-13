from typing import Any, Optional
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.base_user import AbstractBaseUser
from django.http import HttpRequest
from django.contrib.auth import get_user_model

User = get_user_model()


class EmailBackend(ModelBackend):
    def authenticate(
        self,
        request: HttpRequest,
        username: Optional[str] = None,
        password: str = None,
        **kwargs: Any
    ) -> Optional[AbstractBaseUser]:
        email = kwargs.get("email")
        if email is None:
            return None
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return None

        if user.check_password(password):
            return user
        return None
