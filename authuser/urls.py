from django.urls import path
from . import views

urlpatterns = [
    path("create_user/", views.UserCreation.as_view(), name="create_user"),
    path("authenticate_user/", views.UserLogin.as_view(), name="authenticate_user"),
]