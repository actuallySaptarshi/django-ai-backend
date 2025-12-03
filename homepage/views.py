from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages  # Import the messages framework
from .models import users, contact_form
from . import forms

def index(request):
    if request.method == 'POST':
        form = forms.CreateMessage(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!') # Add a success message
            return redirect('index')
    else:
        form = forms.CreateMessage()

    try:
        User = users.objects.get(name="public")
    except ObjectDoesNotExist:
        User = users.objects.create(name="public", chats=0, promptsAnswered=0)

    context = {
        "chats" : User.chats,
        "prompts_answered" : User.promptsAnswered,
        "form": form
    }
    
    return render(request, 'index.html', context)