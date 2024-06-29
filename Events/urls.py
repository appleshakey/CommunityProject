from django.urls import path
from . import views

urlpatterns = [
    path("create_event/", views.EventCreate.as_view(), name="create_event")
]