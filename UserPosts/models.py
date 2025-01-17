from django.db import models
from django.conf import settings
from Communities.models import Community
import uuid

def upload_loc(instance, filename):
    return f'files/{filename}'

# Create your models here.
class UserPost(models.Model):
    id = models.UUIDField(editable=False, primary_key=True, default=uuid.uuid4)
    media = models.FileField(upload_to=upload_loc, default="")
    description = models.TextField(max_length=500)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    community = models.ForeignKey(Community, on_delete=models.CASCADE, default="")

class Comments(models.Model):
    id = models.UUIDField(editable=False, primary_key=True, default=uuid.uuid4)
    comment = models.TextField(max_length=500)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(UserPost, on_delete=models.CASCADE, default="")
    community = models.ForeignKey(Community, on_delete=models.CASCADE, default="")