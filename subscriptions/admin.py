from django.contrib import admin

from .models import Subscription

# Register your models here.

class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ['__unicode__', 'timestamp', 'updated']
    class Meta:
        model = Subscription

admin.site.register(Subscription, SubscriptionAdmin)