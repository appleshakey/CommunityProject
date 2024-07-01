from django.urls import path
from . import views

urlpatterns = [
    path("create_event/", views.EventCreate.as_view(), name="create_event"),
    path("get_all_event/", views.GetAllEvents.as_view(), name="get_all_events"),
    path("get_event/", views.GetInduvidualEvent.as_view(), name="get_event"),
]