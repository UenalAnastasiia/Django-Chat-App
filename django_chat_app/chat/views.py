from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core import serializers
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from .models import Message, Chat
from django.contrib.auth import authenticate, login, logout
from itertools import chain

@login_required(login_url='/login/')
def chat_view(request): 
    Chat.objects.get_or_create(id=1) 
    if request.method == 'POST': 
        myChat = Chat.objects.get(id=1) 
        recipient_list_length = len(list(User.objects.values_list('username', flat=True)))
        if recipient_list_length == 1:
            recipientName = request.user.username
        else:
            recipientName = request.session.get('recipientName')
            
        new_message = Message.objects.create(
            text=request.POST['textmessage'], 
            chat=myChat, 
            author=request.user, 
            recipient=recipientName) 
        serialized_message = serializers.serialize('json', [ new_message ])
        return JsonResponse(serialized_message[1:-1], safe=False)
    chatMessage = Message.objects.filter(author=request.user.id, recipient=request.user.username).order_by('created_at_time', 'created_at')
    return render(request, 'chat/chatroom.html', {'userMessages': chatMessage, 'chatroomName': request.user})


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


def chatroom_view(request, linkname):
    choosenUser = User.objects.get(username = linkname)
    request.session['recipientName'] = choosenUser.username
    chatMessage1 = Message.objects.filter(author=request.user.id, recipient=choosenUser.username)
    chatMessage2 = Message.objects.filter(author=choosenUser.id, recipient=request.user.username)
    if choosenUser == request.user:
       chatMessage = Message.objects.filter(author=choosenUser.id, recipient=choosenUser.username)
       return render(request, 'chat/chatroom.html', {'userMessages': chatMessage, 'chatroomName': choosenUser}) 
    else:
        if len(chatMessage1) == 0:
            chatMessage = chatMessage2
            return render(request, 'chat/chatroom.html', {'userMessages': chatMessage, 'chatroomName': choosenUser})
        else: 
            chatMessage = sorted(chain(chatMessage1, chatMessage2), key=lambda instance: instance.created_at_time)
            return render(request, 'chat/chatroom.html', {'userMessages': chatMessage, 'chatroomName': choosenUser})