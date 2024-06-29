from django.urls import path
from . import views

urlpatterns = [
    path("create_news/", views.NewsCreation.as_view(), name="create_news"),
]