from django.db import models
from django.conf import settings
import uuid

# Create your models here.

def upload_to(instance, filename):
    return f'community/{filename}'

class Community(models.Model):
    id = models.UUIDField(editable=False, primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=500, blank=False)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=False)
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="members")
    secret_key = models.CharField(max_length=100, default = "", unique=True)
    photo = models.FileField(upload_to=upload_to, blank=True)
