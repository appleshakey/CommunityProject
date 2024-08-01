from django.db import models
from django.conf import settings
from Communities.models import Community
import uuid

# Create your models here.

def upload_loc(instance, filename):
    return f'publicPost/{filename}'

# Create your models here.
class PublicPost(models.Model):
    id = models.UUIDField(editable=False, primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=100, default="")
    description = models.TextField(max_length=500)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Post(models.Model):
    id = models.UUIDField(editable=False, primary_key=True, default=uuid.uuid4)
    media = models.FileField(upload_to=upload_loc)
    public_post = models.ForeignKey(PublicPost, on_delete=models.CASCADE)
