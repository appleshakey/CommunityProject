from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework import status
from .models import PublicPost, Post
from .serializer import PublicPostSerializer, PostSerializer
import json

# Create your views here.
class CreatePublicPost(APIView):
    def post(self, request): # title, description, array of media needed!!
        if request.user.is_authenticated:
            data = {
                "id": "",
                "title": request.data["title"],
                "description": request.data["description"],
                "user": request.user.id
            }
            serializer = PublicPostSerializer(data = data)
            if serializer.is_valid():
                serializer.save()
                for i in range(1, int(request.data["no_of_media"])+1):
                    data = {
                        "id": "",
                        "media": request.data[f"post {str(i)}"],
                        "public_post": serializer.data["id"]
                    }
                    print(data["media"])
                    post_serializer = PostSerializer(data=data)
                    if post_serializer.is_valid():
                        post_serializer.save()
                    else:
                        return Response(json.dumps({"message": "posts are not valid"}), status=status.HTTP_400_BAD_REQUEST)
                return Response(json.dumps({"message": "public post posted"}), status=status.HTTP_201_CREATED)
            else:
                return Response(json.dumps({"error": "could not post"}), status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(json.dumps({"error": "unauthorized"}), status=status.HTTP_401_UNAUTHORIZED)
        
        # return Response(status=status.HTTP_200_OK) 

       
class RetrieveAllPosts(APIView):
    def get(self, request):
        postItems = PublicPost.objects.all()[::-1]
        response = []
        for i in postItems:
            posts = Post.objects.filter(public_post = i)
            media = []
            for j in posts:
                media.append({"media": "/files/"+j.media.name, "id": str(j.id)})
            post = {"id": str(i.id), "media": media, "title": i.title, "description": i.description, "user": i.user.username}
            response.append(post)
        return Response(json.dumps(response), status=status.HTTP_200_OK)
        
