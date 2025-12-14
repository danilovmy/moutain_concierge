from django.contrib import admin

from .models import Partner


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ("name", "type", "region", "status")
    list_filter = ("type", "status", "region")
    search_fields = ("name", "phone", "whatsapp", "email", "region")


# Register your models here.
