from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render

from register.models import RegisterForm


def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            user = form.save()
            
            user.is_valid = False
            return redirect("/login")
        else:
            return render(response, 'register/register.html', {'form': form})
    else:
        form = RegisterForm()

    return render(response, "register/register.html", {"form": form})