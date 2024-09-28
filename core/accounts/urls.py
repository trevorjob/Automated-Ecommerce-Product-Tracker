from django.urls import path
from .views import CreateListUsersView

urlpatterns = [
    path("users/", view=CreateListUsersView.as_view(), name="create_list_users")
]
