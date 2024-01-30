from django.db import models
from datetime import date
from django.conf import settings

# Create your models here

class Chat(models.Model):
    created_at = models.DateField(default=date.today)
    # receiver = models.CharField(max_length=500)
    # author = models.ForeignKey(
    #     settings.AUTH_USER_MODEL,
    #     on_delete=models.CASCADE, 
    #     related_name='chat_message_set'
    # )
    
class Message(models.Model):
    text = models.CharField(max_length=500)
    created_at = models.DateField(default=date.today)

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

    receiver = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='receiver_message_set'
    )
