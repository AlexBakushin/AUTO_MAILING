from django.contrib import admin
from main.models import Client, Settings, Massage


@admin.register(Client)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'mail',)
    list_filter = ('last_name',)
    search_fields = ('first_name', 'last_name', 'mail',)


@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ('time', 'frequency', 'status')
    list_filter = ('status',)
    search_fields = ('status', 'frequency',)


@admin.register(Massage)
class MassageAdmin(admin.ModelAdmin):
    list_display = ('head', 'body',)
    list_filter = ('head',)
    search_fields = ('head',)
