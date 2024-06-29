from rest_framework import serializers
from .models import UserPost, Comments

class UserPostsSerializer(serializers.ModelSerializers):
    class Meta:
        model = UserPost
        fields = ["id", "image", "description", "user"]

class CommentsSerializer(serializers.ModelSerializers):
    class Meta:
        model = Comments
        fields = ["id", "comment", "user", "post"]