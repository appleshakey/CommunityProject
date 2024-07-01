from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework import status
from .models import Events
from .serializer import EventsSerializer
from Communities.models import Community
from authuser.models import User
import json
# Create your views here.

class EventCreate(APIView):
    def post(self, request):
        if request.user.is_authenticated:
            title = request.data["title"]
            description = request.data["description"]
            event_time = request.data["event_time"]
            community = Community.objects.get(name=request.data["community_name"])
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
            user = User.objects.get(email=request.user.email)
            members = user.members.all()
            owners = Community.objects.filter(owner = user)
            community = Community.objects.get(name = request.data["community_name"])
            if community in list(members) or community in list(owners):
                events = Events.objects.filter(community = community)
                serializer = EventsSerializer(events, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(json.dumps({"error": "cannot get"}), status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(json.dumps({"error": "unauthorized"}, status=status.HTTP_401_UNAUTHORIZED))

class GetInduvidualEvent(APIView):
    def post(self, request):
        if request.user.is_authenticated:
            user = User.objects.get(email=request.user.email)
            members = user.members.all()
            owners = Community.objects.filter(owner = user)
            event = Events.objects.get(id = request.data["id"])
            if event.community in list(members) or event.community in list(owners):
                serializer = EventsSerializer(event)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(json.dumps({"error": "cannot get"}), status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(json.dumps({"error": "unauthorized"}), status=status.HTTP_401_UNAUTHORIZED)
    
    def get(self, request):
        user = User.objects.get(email=request.user.email)
        members = user.members.all()
        owners = Community.objects.filter(owner = user)
        print(members, owners)
        return Response("OK")
        