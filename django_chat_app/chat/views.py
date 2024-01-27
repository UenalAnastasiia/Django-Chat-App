from django.shortcuts import render
from .models import Message, Chat

def index(request):
    if request.method == 'POST':             
        print(request.POST['textmessage'])
        myChat = Chat.objects.get(id=1)
        Message.objects.create(
            text=request.POST['textmessage'], 
            chat=myChat, 
            author=request.user,
            receiver=request.user)
    chatMessage = Message.objects.filter(chat__id=1)
    return render(request, 'chat/index.html', {'messages': chatMessage})
