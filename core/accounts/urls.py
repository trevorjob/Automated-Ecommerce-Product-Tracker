from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import CreateListUsersView, LoginView, RegisterView

urlpatterns = [
    path(
        "auth/token/",
        view=TokenObtainPairView.as_view(),
        name="retrieve access and refresh tokens",
    ),
    path(
        "auth/token/refresh/",
        view=TokenRefreshView.as_view(),
        name="token_refresh",
    ),
    path("users/", view=CreateListUsersView.as_view(), name="create_list_users"),
    path("auth/login/", view=LoginView.as_view(), name="login"),
    path("auth/register/", view=RegisterView.as_view(), name="register"),
]
