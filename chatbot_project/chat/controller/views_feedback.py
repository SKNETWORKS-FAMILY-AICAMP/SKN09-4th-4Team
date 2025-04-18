from django.shortcuts import render
from django.shortcuts import redirect
from chat.forms import FeedbackForm
from chat.service.feedback_service import save_feedback

def feedback_submit(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            save_feedback(form.cleaned_data)
    return redirect('chat_page')
