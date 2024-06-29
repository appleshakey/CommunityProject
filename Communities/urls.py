from django.urls import path
from . import views

urlpatterns = [
    path("create_community/", views.CreateCommunity.as_view(), name="create_community"),
    path("join_community/", views.JoinCommunity.as_view(), name="join_community"),
    path("show_community/", views.ShowCommunities.as_view(), name="show_community")
]