from django.urls import path
from . import views

urlpatterns = [
    path("create_news/", views.NewsCreation.as_view(), name="create_news"),
    path("show_all_news/", views.ShowAllNews.as_view(), name="show_all_news"),
    path("show_news/", views.ShowInduvidualNews.as_view(), name="show_news"),
]