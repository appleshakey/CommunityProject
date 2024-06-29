from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework import status
from .models import PublicPost
from .serializer import PublicPostSerializer
import json

# Create your views here.
class CreatePublicPost(APIView):
    def post(self, request):
        if request.user.is_authenticated:
            data = {
                "id": "",
                "media": request.data["media"],
                "title": request.data["title"],
                "description": request.data["description"],
                "user": request.user.id
            }
            serializer = PublicPostSerializer(data = data)
            if serializer.is_valid():
                serializer.save()
                return Response(json.dumps({"message": "public post posted"}), status=status.HTTP_201_CREATED)
            else:
                return Response(json.dumps({"error": "could not post"}), status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(json.dumps({"error": "unauthorized"}), status=status.HTTP_401_UNAUTHORIZED)
        
class RetrieveAllPosts(APIView):
    def get(self, request):
        publicPosts = PublicPost.objects.all()
        serializer = PublicPostSerializer(publicPosts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
