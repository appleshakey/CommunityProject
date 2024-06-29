from django.db import models
from django.utils import timezone
import uuid
from django.conf import settings
from Communities.models import Community

# Create your models here.
class Events(models.Model):
    id = models.UUIDField(editable=False, primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length = 100, unique=True)
    description = models.TextField(max_length = 500)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL)
    community = models.ForeignKey(Community, on_delete=models.CASCADE, default="")
    event_time = models.TextField(max_length=100, blank=True)
    created_now = models.DateTimeField(default=timezone.now)
    
