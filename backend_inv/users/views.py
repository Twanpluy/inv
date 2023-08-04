from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import RegisterSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics

# class view get user details and token auth

class UserDetailAPI(APIView):
    authentication_classes = [TokenAuthentication,]
    permission_classes = [AllowAny,]
    
    # get user details method
    def get(self, request, *args, **kwargs):
        user = User.objects.get(id=request.user.id)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    

# class view register user
class RegisterUserAPIView(generics.CreateAPIView):
    permission_classes = [AllowAny,]
    serializer_class = RegisterSerializer