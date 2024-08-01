from rest_framework import serializers
from .models import PublicPost, Post

class PublicPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublicPost
        fields = ["id", "title", "description", "user"]
    
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["id", "media", "public_post"]