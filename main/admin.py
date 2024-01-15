from django.contrib import admin
from main.models import Client, Settings, Massage, Logs


@admin.register(Client)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'mail', 'massage')
    list_filter = ('name',)
    search_fields = ('name', 'mail', 'massage')


@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ('time', 'frequency', 'status')
    list_filter = ('status',)
    search_fields = ('status', 'frequency',)


@admin.register(Massage)
class MassageAdmin(admin.ModelAdmin):
    list_display = ('head', 'body', 'settings')
    list_filter = ('head',)
    search_fields = ('head',)


@admin.register(Logs)
class LogsAdmin(admin.ModelAdmin):
    list_display = ('datatime', 'status', 'response')
    list_filter = ('status',)
    search_fields = ('status', 'response',)
