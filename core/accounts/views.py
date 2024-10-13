# from rest_framework.authentication import  authenticate
from django.contrib.auth import authenticate
from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import *
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import User
from .serializers import UserRegisterserializer
from .tokens import create_jwt

# Create your views here.


class CreateListUsersView(APIView):
    def get(self, request: Request, *args, **kwargs):
        return Response({"message": "get a list of users"})

    def post(self, request: Request, *args, **kwargs):
        return Response("create a user")


class LoginView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]

    def post(self, request: Request):

        email = request.data.get("email")
        password = request.data.get("password")
        user = authenticate(email=email, password=password)
        if user is None:
            return Response(
                data={"error": "user not found"}, status=status.HTTP_404_NOT_FOUND
            )

        tokens = create_jwt(user)
        response = {"message": "login successfully", "tokens": tokens}

        return Response(data=response, status=status.HTTP_200_OK)


class RegisterView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    serializer_class = UserRegisterserializer

    def post(self, request: Request, *args, **kwargs):
        # try:
        data = request.data

        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                {
                    "success": True,
                    "message": "user successfully created",
                    "data": serializer.data,
                },
                status=status.HTTP_201_CREATED,
            )

        return Response(
            {"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
        )
