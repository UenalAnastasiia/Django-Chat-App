from django.contrib.auth.models import User


def receiverList(request):
    receiverList = list(User.objects.values_list('username', flat=True))
    return {"receiverList": receiverList}