from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from .models import Message, Chat
from django.contrib.auth import authenticate, login, logout

@login_required(login_url='/login/')
def chat_view(request):  
    if request.method == 'POST': 
        myChat = Chat.objects.get(id=1)
        new_message = Message.objects.create(
            text=request.POST['textmessage'], 
            chat=myChat, 
            author=request.user, 
            receiver=request.user) 
        serialized_message = serializers.serialize('json', [ new_message ])
        return JsonResponse(serialized_message[1:-1], safe=False)

    chatMessage = Message.objects.filter(chat__id=1)
    return render(request, 'chat/chatroom.html', {'messages': chatMessage})


def login_view(request):
    if request.method == 'POST':   
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/chat/')
        else:
            return render(request, 'auth/login.html', {'wrong_password': True})
    return render(request, 'auth/login.html')


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/login/')