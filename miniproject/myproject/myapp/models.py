from django.core.exceptions import ValidationError
from django.db import models


class Production(models.Model):
    class Status(models.TextChoices):
        PLANNING = "planning", "Planning"
        IN_PRODUCTION = "in_production", "In production"
        COMPLETED = "completed", "Completed"
        ON_HOLD = "on_hold", "On hold"

    name = models.CharField(max_length=150)
    client = models.CharField(max_length=150)
    status = models.CharField(
        max_length=20, choices=Status.choices, default=Status.PLANNING
    )
    start_date = models.DateField()
    end_date = models.DateField()
    budget = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["start_date", "name"]
        verbose_name_plural = "productions"

    def __str__(self):
        return self.name

    def clean(self):
        super().clean()
        if self.start_date and self.end_date and self.end_date < self.start_date:
            raise ValidationError({"end_date": "End date cannot be before start date."})


class Event(models.Model):
    class Category(models.TextChoices):
        WEDDING = "wedding", "Wedding"
        MUSIC_CONCERT = "music_concert", "Music concert"
        CORPORATE = "corporate", "Corporate event"
        BIRTHDAY = "birthday", "Birthday"
        CONFERENCE = "conference", "Conference"
        OTHER = "other", "Other"

    class Status(models.TextChoices):
        SCHEDULED = "scheduled", "Scheduled"
        COMPLETED = "completed", "Completed"
        CANCELLED = "cancelled", "Cancelled"

    production = models.ForeignKey(
        Production, on_delete=models.PROTECT, related_name="events"
    )
    category = models.CharField(
        max_length=20, choices=Category.choices, default=Category.OTHER
    )
    name = models.CharField(max_length=150)
    event_date = models.DateField()
    start_time = models.TimeField()
    venue = models.CharField(max_length=200)
    status = models.CharField(
        max_length=20, choices=Status.choices, default=Status.SCHEDULED
    )
    attendees = models.PositiveIntegerField(default=0)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["event_date", "start_time", "name"]

    def __str__(self):
        return self.name


class EventBooking(models.Model):
    class Status(models.TextChoices):
        NEW = "new", "New request"
        CONTACTED = "contacted", "Client contacted"
        CONFIRMED = "confirmed", "Confirmed"
        DECLINED = "declined", "Declined"

    class Category(models.TextChoices):
        WEDDING = "wedding", "Wedding"
        MUSIC_CONCERT = "music_concert", "Music concert"
        CORPORATE = "corporate", "Corporate event"
        BIRTHDAY = "birthday", "Birthday"
        CONFERENCE = "conference", "Conference"
        OTHER = "other", "Other"

    customer_name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=30)
    category = models.CharField(max_length=20, choices=Category.choices)
    event_date = models.DateField()
    guest_count = models.PositiveIntegerField()
    venue = models.CharField(max_length=200)
    details = models.TextField(blank=True)
    status = models.CharField(
        max_length=20, choices=Status.choices, default=Status.NEW
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "event booking request"
        verbose_name_plural = "event booking requests"

    def __str__(self):
        return f"{self.get_category_display()} booking from {self.customer_name}"
