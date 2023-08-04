from django.urls import path
from .views import RegisterView

urlpatterns = [
    path("register", RegisterView.as_view(), name="register"),
    path("login", RegisterView.as_view(), name="login"),
    path("logout", RegisterView.as_view(), name="logout"),
    path("password", RegisterView.as_view(), name="password"),
    path("reset-password", RegisterView.as_view(), name="reset-password"),
]
