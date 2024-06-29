from django.urls import path
from . import views

urlpatterns = [
    path("create_public_post/", views.CreatePublicPost.as_view(), name="create_public_post"),
    path("show_public_posts/", views.RetrieveAllPosts.as_view(), name="show_all_public_posts"),
]