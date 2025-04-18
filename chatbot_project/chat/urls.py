from django.urls import path
from chat.controller import views_chat

urlpatterns = [
    path("intro/", views_chat.intro_view, name="intro_page"),
    path("chat/", views_chat.chat_view, name="chat_page"),
]
