from django import forms

from .models import Event, EventBooking, Production


class DateInput(forms.DateInput):
    input_type = "date"


class TimeInput(forms.TimeInput):
    input_type = "time"


class ProductionForm(forms.ModelForm):
    class Meta:
        model = Production
        fields = [
            "name",
            "client",
            "status",
            "start_date",
            "end_date",
            "budget",
            "description",
        ]
        widgets = {
            "start_date": DateInput(),
            "end_date": DateInput(),
            "description": forms.Textarea(attrs={"rows": 4}),
        }


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            "production",
            "name",
            "event_date",
            "start_time",
            "venue",
            "status",
            "attendees",
            "notes",
        ]
        widgets = {
            "event_date": DateInput(),
            "start_time": TimeInput(),
            "notes": forms.Textarea(attrs={"rows": 4}),
        }


class EventBookingForm(forms.ModelForm):
    class Meta:
        model = EventBooking
        fields = [
            "customer_name",
            "email",
            "phone",
            "category",
            "event_date",
            "guest_count",
            "venue",
            "details",
        ]
        widgets = {
            "event_date": DateInput(),
            "details": forms.Textarea(attrs={"rows": 4}),
        }
