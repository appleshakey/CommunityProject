from django.db import models
from django.conf import settings
import uuid

def upload_loc(instance, filename):
    return f'files/{filename}'

# Create your models here.
class Posts(models.Model):
    id = models.UUIDField(editable=False, primary_key=True, default=uuid.uuid4)
    image = models.ImageField(upload_to=upload_loc)
    description = models.TextField(max_length=500)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    

class Comments(models.Model):
    id = models.UUIDField(editable=False, primary_key=True, default=uuid.uuid4)
    comment = models.TextField(max_length=500)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)