# Generated by Django 5.0.1 on 2024-01-31 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_message_chat'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='recipient',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
