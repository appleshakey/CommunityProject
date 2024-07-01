from django.urls import path
from . import views

urlpatterns = [
    path("create_post/", views.UserPostCreation.as_view(), name="create_post"),
    path("show_all_post/", views.ShowAllUserPost.as_view(), name="show_all_posts"),
    path("show_post/", views.ShowInduvidualPost.as_view(), name="show_post"),
]
