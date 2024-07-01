from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework import status
from .models import UserPost
from authuser.models import User
from Communities.models import Community
from .serializer import UserPostsSerializer
import json

# Create your views here.
class UserPostCreation(APIView):
    def post(self, request):
        if request.user.is_authenticated:
            user = User.objects.get(email=request.user.email)
            owner_comms = Community.objects.filter(owner=user)
            member_comms = user.members.all()
            community = Community.objects.get(name=request.data["community_name"])
            data = {
                "media": request.data["media"],
                "description": request.data["description"],
                "user": request.user.id,
                "community": community.id,
            }
            if community in list(owner_comms) or community in list(member_comms):
                serializer = UserPostsSerializer(data=data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(json.dumps({"message": "post is saved"}), status=status.HTTP_201_CREATED)
                else:
                    return Response(json.dumps({"error": "bad request"}), status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(json.dumps({"error": "cannot post"}), status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(json.dumps({"error": "unauthorized"}), status=status.HTTP_401_UNAUTHORIZED)
        
class ShowAllUserPost(APIView):
    def post(self, request):
        if request.user.is_authenticated:
            user = User.objects.get(email = request.user.email)
            owner_comms = Community.objects.filter(owner=user)
            member_comms = user.members.all()
            community = Community.objects.get(name = request.data["community_name"])
            if community in list(owner_comms) or community in list(member_comms):
                posts = UserPost.objects.filter(community=community)
                serializer = UserPostsSerializer(posts, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(json.dumps({"error": "cannot get"}), status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(json.dumps({"error": "unauthorized"}), status=status.HTTP_401_UNAUTHORIZED)

class ShowInduvidualPost(APIView):
    def post(self, request):
        if request.user.is_authenticated:
            user = User.objects.get(email=request.user.email)
            owner_comms = Community.objects.filter(owner=user)
            member_comms = user.members.all()
            post = UserPost.objects.get(id=request.data["id"])
            if post.community in list(owner_comms) or post.community in list(member_comms):
                serializer =  UserPostsSerializer(post)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(json.dumps({"error": "cannot get"}), status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(json.dumps({"error": "unauthorized"}), status=status.HTTP_401_UNAUTHORIZED) 