from rest_framework import serializers
from .models import UserPost, Comments

class UserPostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPost
        fields = ["id", "media", "description", "user", "community"]

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ["id", "comment", "user", "post"]