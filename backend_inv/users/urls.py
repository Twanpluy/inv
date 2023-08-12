from django.urls import path
from .views import RegisterUserAPIView,LoginUserAPIView,UserDetailAPIView

urlpatterns = [
    path('login', LoginUserAPIView.as_view()),
    path('register', RegisterUserAPIView.as_view()),
    path('user', UserDetailAPIView.as_view()),
]
