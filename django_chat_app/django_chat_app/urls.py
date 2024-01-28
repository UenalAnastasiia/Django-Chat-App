"""
URL configuration for django_chat_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from chat.views import chat_view, login_view, logout_view, send_message_to_DB
from register import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/', chat_view),
    path('chat/send/', send_message_to_DB),
    path('login/', login_view),
    path('logout/', logout_view),
    path("register/", v.register),
]
