from django.contrib import admin

from .models import Booking, BookingItem


class BookingItemInline(admin.TabularInline):
    model = BookingItem
    extra = 1


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("id", "guest_name", "lead", "date_from", "date_to", "status")
    list_filter = ("status", "date_from", "date_to")
    search_fields = ("guest_name",)
    inlines = [BookingItemInline]


@admin.register(BookingItem)
class BookingItemAdmin(admin.ModelAdmin):
    list_display = ("booking", "service_type", "partner", "guest_price", "commission")
    list_filter = ("service_type", "partner")


# Register your models here.
