from django.urls import path

from . import views

urlpatterns = [
    path("", views.EventBookingCreateView.as_view(), name="booking-create"),
    path("book-event/", views.EventBookingCreateView.as_view(), name="booking-page"),
    path("booking-success/", views.EventBookingSuccessView.as_view(), name="booking-success"),
]
