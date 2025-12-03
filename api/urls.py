from django.urls import path
from . import views

urlpatterns = [
    path("test/", views.Test.as_view(), name="Test"),
    path("chat/", views.Chat.as_view(), name="Chat")
]
