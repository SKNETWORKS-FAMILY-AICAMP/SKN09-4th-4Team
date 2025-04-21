# llm/urls.py

from django.urls import path
from llm.controller.views_llm import ask_llm

urlpatterns = [
    path("ask_llm/", ask_llm, name="ask_llm"),
]
