from django.shortcuts import render
from .models import Message

# Create your views here.
def chat_view(request):
    messages = Message.objects.all()
    return render(request, 'home/index.html', {'messages': messages})