from django.contrib.auth.models import User
from chat.models import Message


def receiverList(request):
    receiverList = list(User.objects.values_list('username', flat=True))
    request.session['receiverListNames'] = receiverList
    return {"receiverList": receiverList}


def chatMessagesLength(request):
    receiverListNames = request.session.get('receiverListNames')
    messagesLength = []
    for receiver in receiverListNames:
        choosenUser = User.objects.get(username = receiver)
        chatMessage1 = len(Message.objects.filter(author=request.user.id, recipient=choosenUser.username))
        chatMessage2 = len(Message.objects.filter(author=choosenUser.id, recipient=request.user.username))
        if receiver == request.user.username:
            messagesLength.append(chatMessage1)
        else:
            messagesLength.append(chatMessage1 + chatMessage2)
    request.session['messagesLength'] = messagesLength
    return {"messagesLength": messagesLength}


def baseMenuListData(request):
    nameList = request.session.get('receiverListNames')
    messagesLength = request.session.get('messagesLength')
    baseListData = []
    for i in range(len(nameList)):
        baseListData.append({'messagesLength': messagesLength[i], 'name': nameList[i]})
        
    return {"baseListData": baseListData}