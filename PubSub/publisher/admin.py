from django.contrib import admin
from publisher.models import PublisherModel
# Register your models here.

@admin.register(PublisherModel)
class PublisherAdmin(admin.ModelAdmin):
    pass