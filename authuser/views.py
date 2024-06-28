from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login, logout
from django.middleware.csrf import get_token
from .models import User
import json

# Create your views here.

class UserCreation(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        name = request.data['name']
        contact = request.data['contact']
        user = User.objects.create_user(email=email, password=password, name=name, contact=contact)
        user = User.objects.get(email=email)
        if user:
            token = Token.objects.create(user=user)
            return Response(json.dumps({"message": "account created!!"}), status=status.HTTP_201_CREATED)


class UserLogin(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        user = authenticate(email = email, password= password)
        if user:
            token = Token.objects.get(user=user)
            return Response(json.dumps({"token": token.key}), status=status.HTTP_200_OK)
        else:
            return Response(json.dumps({"error": "wrong email or password"}), status=status.HTTP_400_BAD_REQUEST)