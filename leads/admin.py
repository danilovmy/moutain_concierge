from django.contrib import admin

from .models import Lead


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ("guest_name", "created_at", "source_type", "status")
    list_filter = ("status", "source_type", "created_at")
    search_fields = ("guest_name", "contact", "source_text")


# Register your models here.
