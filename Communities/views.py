from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework import status
from .models import Community
from authuser.models import User
from .serializer import CommunitySerializer
import json
import uuid
# Create your views here.

class CreateCommunity(APIView):
    def post(self, request):
        if request.user.is_authenticated:
            data = {
                "name": request.data["name"],
                "description": request.data["description"],
                "owner": request.user.id,
            }
            key = uuid.uuid4()
            data["secret_key"] = (str(key)[:8])
            serializer = CommunitySerializer(data = data)
            if serializer.is_valid():
                serializer.save()
                return Response(json.dumps({"message" : "community created"}), status=status.HTTP_201_CREATED)
            else:
                return Response(json.dumps({"error" : "not created"}), status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(json.dumps({"error": "user not logged in"}), status = status.HTTP_401_UNAUTHORIZED)

class JoinCommunity(APIView):
    def post(self, request):
        if request.user.is_authenticated:
            key = request.data["secret_key"]
            community = Community.objects.get(secret_key = key)
            try:
                user = User.objects.get(email = request.user.email)
                community.members.add(user)
                return Response(json.dumps({"message": "joined community"}), status=status.HTTP_200_OK)
            except:
                return Response(json.dumps({"message" : "error in joining community"}), status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(json.dumps({"message": "unauthorized"}), status=status.HTTP_401_UNAUTHORIZED)
        
class ShowCommunities(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            user = User.objects.get(email = request.user.email)
            communities = user.members.all()
            serializer = CommunitySerializer(communities, many = True)
            if serializer:
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(json.dumps({"error": "no data found"}), status = status.HTTP_404_NOT_FOUND)
        else:
            return Response(json.dumps({"error": "unauthorized"}), status = status.HTTP_401_UNAUTHORIZED)
            

            