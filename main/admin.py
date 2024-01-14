from django.contrib import admin

from main.models import Client, Settings, Massage, Logs

admin.site.register(Client)
admin.site.register(Settings)
admin.site.register(Massage)
admin.site.register(Logs)
