# Generated by Django 5.0.1 on 2024-01-31 12:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0005_remove_message_receiver'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='created_at_time',
            field=models.TimeField(default=datetime.datetime.now, null=True),
        ),
    ]