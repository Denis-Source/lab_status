from django.contrib import admin
from message.models import Message


class MessageAdmin(admin.ModelAdmin):
    list_display = ("id", "author", "time")


admin.site.register(Message, MessageAdmin)
