from django.contrib.auth.models import User
from django.db import models
from datetime import date, datetime
from django.conf import settings

# Create your models here

class Chat(models.Model):
    created_at = models.DateField(default=date.today)
    
class Message(models.Model):
    text = models.CharField(max_length=500)
    created_at = models.DateField(default=date.today)
    created_at_time = models.TimeField(default=datetime.now, null=True)
    recipient = models.CharField(max_length=100, null=True)

    chat = models.ForeignKey(
        Chat,
        on_delete=models.CASCADE, 
        related_name='chat_message_set',
        # Standartwert einer Nachricht ist None
        default=None,
        # Es wird erlaubt leere Werte einzugeben
        blank=True,
        # Damit akzeptiert die Datenbank Null-Werte
        null=True
    )

    # zeigt Namen von den registrierten Users
    # on_delete=models.CASCADE => löscht z.B. die Nachricht, wenn der User gelöscht wurde
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, 
        related_name='author_message_set'
    )