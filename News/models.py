from django.db import models
from django.utils import timezone
import uuid
from Communities.models import Community

# Create your models here.
class News(models.Model):
    id = models.UUIDField(editable=False, primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    created_now = models.DateTimeField(default=timezone.now)
    community = models.ForeignKey(Community, on_delete = models.CASCADE, default="")

    def newsTitle(self):
        return self.title
