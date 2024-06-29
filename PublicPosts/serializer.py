from rest_framework import serializers
from .models import PublicPost

class PublicPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublicPost
        fields = ["id", "media", "title", "description", "user"]