# chat/urls.py

from django.urls import path
from chat.controller import views_chat
from chat.controller.views_feedback import save_feedback_view

app_name = 'chat'

urlpatterns = [
    path("intro/", views_chat.intro_view, name="intro_page"),
    path("chat/", views_chat.chat_view, name="chat_page"),
    path("chat/feedback/", save_feedback_view, name="save_feedback"),
    path("chat/ask_llm/", views_chat.ask_llm_view, name="ask_llm"),
    ]
