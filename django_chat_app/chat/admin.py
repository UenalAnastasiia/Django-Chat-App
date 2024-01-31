from django.contrib import admin
from .models import Chat, Message

class MessageAdmin(admin.ModelAdmin):
    fields = ('chat','text','created_at', 'author', 'recipient', 'created_at_time')
    list_display = ('created_at', 'author', 'text', 'recipient')
    search_fields = ('text',)


# Register your models here.
admin.site.register(Message, MessageAdmin)
admin.site.register(Chat)