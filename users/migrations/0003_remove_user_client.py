# Generated by Django 5.0.1 on 2024-01-20 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_client_alter_user_avatar_alter_user_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='client',
        ),
    ]
