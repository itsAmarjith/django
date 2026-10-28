from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from .forms import EventBookingForm
from .models import EventBooking


class EventBookingCreateView(CreateView):
    model = EventBooking
    form_class = EventBookingForm
    template_name = "myapp/booking_form.html"
    success_url = reverse_lazy("booking-success")


class EventBookingSuccessView(TemplateView):
    template_name = "myapp/booking_success.html"
