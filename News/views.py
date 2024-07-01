from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework import status
from .models import News
from Communities.models import Community
from .serializer import NewsSerializer
from authuser.models import User
import json

# Create your views here.
class NewsCreation(APIView):
    def post(self, request):
        if request.user.is_authenticated:
            title = request.data["title"]
            description = request.data["description"]
            community = Community.objects.get(name=request.data["community_name"])
            data={
                "title": title,
                "description": description,
                "community": community.id,
            }
            if community.owner == request.user:
                serializer = NewsSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(json.dumps({"message": "News successfully created"}), status = status.HTTP_201_CREATED)
                else:
                    return Response(status = status.HTTP_400_BAD_REQUEST)
            else:
                return Response(json.dumps({"error": "cannot post"}), status=status.HTTP_401_UNAUTHORIZED)

        else:
            return Response(json.dumps({"message": "user not logged in"}))

class ShowAllNews(APIView):
    def post(self, request):
        if request.user.is_authenticated:
            user = User.objects.get(email = request.user.email)
            owner_comms = Community.objects.filter(owner=request.user)
            member_comms = user.members.all()
            community = Community.objects.get(name = request.data["community_name"])
            if community in list(owner_comms) or community in list(member_comms):
                news = News.objects.filter(community = community)
                serializer = NewsSerializer(news, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(json.dumps({"error" : "cannot get"}), status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(json.dumps({"error": "unauthorized"}), status = status.HTTP_401_UNAUTHORIZED)

class ShowInduvidualNews(APIView):
    def post(self, request):
        if request.user.is_authenticated:
            user = User.objects.get(email=request.user.email)
            owner_comms = Community.objects.filter(owner=request.user)
            member_comms = user.members.all()
            news = News.objects.get(id = request.data["id"])
            if news.community in list(owner_comms) or news.community in list(member_comms):
                serializer = NewsSerializer(news)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(json.dumps({"error": "cannot get"}), status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(json.dumps({"error": "unauthorized"}), status=status.HTTP_401_UNAUTHORIZED)
            