from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate

from .serializer import RegisterSerializer

# class view register user
class RegisterUserAPIView(generics.CreateAPIView):
    permission_classes = [
        AllowAny,
    ]
    serializer_class = RegisterSerializer


# class login user
class LoginUserAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        username = request.data.get('username')
        password = request.data.get('password')

        if username is None or password is None:
            if username is None:
                return Response({'error': 'Please provide username.'}, status=400)
            if password is None:
                return Response({'error': 'Please provide password.'}, status=400)
            
        user = authenticate(username=username, password=password)

        if user is None:
            return Response({'error': 'Invalid credentials.'}, status=400)

        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})


#user details
class UserDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request,format=None):
        user = request.user
        return Response(
            {
                'id':user.id,
                'username':user.username,
                'email':user.email,
            }
        )