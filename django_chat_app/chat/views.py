from django.shortcuts import render

def index(request):
    print(request.method)    
    if request.method == 'POST':             
        print(request.POST['textmessage'])
    return render(request, 'chat/index.html', {'username': 'Anna'})
