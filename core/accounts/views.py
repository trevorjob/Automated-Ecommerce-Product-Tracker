from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import *
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.


class CreateListUsersView(APIView):
    permission_classes = []

    def get(self, request: Request, *args, **kwargs):
        return Response("get a list of users")

    def post(self, request: Request, *args, **kwargs):
        return Response("create a user")
