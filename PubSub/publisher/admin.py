from django.contrib import admin
from publisher.models import PublisherModel, MessageModel
# Register your models here.

@admin.register(PublisherModel)
class PublisherAdmin(admin.ModelAdmin):
    pass

@admin.register(MessageModel)
class MessageAdmin(admin.ModelAdmin):
    pass