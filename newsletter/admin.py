from django.contrib import admin

from newsletter.models import Message, MessageSettings


@admin.register(MessageSettings)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['start_time', ]#'newsletter_time', 'periodicity', 'status']
   # list_filter = ['status']


@admin.register(Message)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['client', 'message_theme']
