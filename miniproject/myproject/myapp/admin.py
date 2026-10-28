from django.contrib import admin

from .models import EventBooking


@admin.register(EventBooking)
class EventBookingAdmin(admin.ModelAdmin):
    list_display = (
        "customer_name",
        "category",
        "event_date",
        "venue",
        "guest_count",
        "status",
        "created_at",
    )
    list_filter = ("category", "status", "event_date")
    search_fields = ("customer_name", "email", "phone", "venue")
    readonly_fields = ("created_at",)
    fieldsets = (
        ("Customer contact", {"fields": ("customer_name", "email", "phone")}),
        ("Event details", {"fields": ("category", "event_date", "guest_count", "venue", "details")}),
        ("Booking management", {"fields": ("status", "created_at")}),
    )
    date_hierarchy = "event_date"
    ordering = ("status", "event_date")
    list_per_page = 25
