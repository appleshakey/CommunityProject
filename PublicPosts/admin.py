from django.contrib import admin
from .models import PublicPost, Post
# Register your models here.

admin.site.register(PublicPost)
admin.site.register(Post)