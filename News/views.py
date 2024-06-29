from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework import status
from .models import News
from .serializer import NewsSerializer
import json

# Create your views here.
class NewsCreation(APIView):
    def post(self, request):
        if request.user.is_authenticated:
            title = request.data["title"]
            description = request.data["description"]
            data={
                "title": title,
                "description": description,
            }
            serializer = NewsSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(json.dumps({"message": "Event successfully created"}), status = status.HTTP_201_CREATED)
            else:
                return Response(status = status.HTTP_400_BAD_REQUEST)
            
        else:
            return Response(json.dumps({"message": "user not logged in"}))