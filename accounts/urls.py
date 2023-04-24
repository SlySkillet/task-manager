from django.urls import path
from .views import login_user, logout_user


urlpatterns = [
    path("logout/", logout_user, name="logout"),
    path("login/", login_user, name="login"),
]
