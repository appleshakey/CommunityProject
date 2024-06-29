from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework import status
from .models import Events
from .serializer import EventsSerializer
from Communities.models import Community
import json
# Create your views here.

class EventCreate(APIView):
    def post(self, request):
        if request.user.is_authenticated:
            title = request.data["title"]
            description = request.data["description"]
            event_time = request.data["event_time"]
            community = Community.objects.get(name=request.data["community_name"])
            print(community.id)
            data={
                "id": "",
                "title": title,
                "description": description,
                "event_time": event_time,
                "community": community.id,
            }
            serializer = EventsSerializer(data=data)
            if serializer.is_valid() and request.user == community.owner:
                serializer.save()
                return Response(json.dumps({"message": "Event successfully created"}), status = status.HTTP_201_CREATED)
            else:
                return Response(status = status.HTTP_400_BAD_REQUEST)
            
        else:
            return Response(json.dumps({"message": "user not logged in"}))
        
class GetAllEvents(APIView):
    def post(self, request):
        if request.user.is_authenticated:
            community = Community.objects.get(name = request.data["name"])
            print(community.members)
            return Response(json.dumps({"OK"}))

        