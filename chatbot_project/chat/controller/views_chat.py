from django.shortcuts import render


def intro_view(request):
    return render(request, "chat/intro.html")

def chat_view(request):
    return render(request, "chat/chat.html")
