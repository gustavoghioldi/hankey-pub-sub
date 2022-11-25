from django.contrib import admin
from subscribers.models import SubscriberModel
# Register your models here.
@admin.register(SubscriberModel)
class SubscriberAdmin(admin.ModelAdmin):
    pass
