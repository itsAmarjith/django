from django.contrib import admin
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import EventBooking


class EventBookingTests(TestCase):
    def test_booking_form_is_the_only_public_interface(self):
        response = self.client.get(reverse("booking-create"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Weddings")
        self.assertContains(response, "Live music")
        self.assertContains(response, "Corporate event")
        self.assertContains(response, "myapp/images/wedding-celebration.jpg")
        self.assertContains(response, "myapp/images/live-music-concert.jpg")
        self.assertContains(response, "Bride and groom celebrating their wedding")
        self.assertContains(response, "Crowd enjoying a live music concert")
        self.assertContains(response, "AJ Productions")
        self.assertContains(response, "jithuaji066@gmail.com")
        self.assertContains(response, "7907443329")
        self.assertContains(response, "Thanal Mullickala")
        self.assertEqual(self.client.get(reverse("booking-page")).status_code, 200)
        self.assertEqual(self.client.get("/productions/").status_code, 404)
        self.assertEqual(self.client.get("/events/").status_code, 404)

    def test_customer_can_submit_booking_request(self):
        response = self.client.post(
            reverse("booking-create"),
            {
                "customer_name": "Avery Jordan",
                "email": "avery@example.com",
                "phone": "555-0100",
                "category": EventBooking.Category.WEDDING,
                "event_date": "2027-06-12",
                "guest_count": 120,
                "venue": "Garden Hall",
                "details": "An outdoor ceremony and reception.",
            },
            follow=True,
        )
        self.assertEqual(response.request["PATH_INFO"], reverse("booking-success"))
        self.assertContains(response, "REQUEST RECEIVED")
        booking = EventBooking.objects.get(email="avery@example.com")
        self.assertEqual(booking.category, EventBooking.Category.WEDDING)
        self.assertEqual(booking.status, EventBooking.Status.NEW)

    def test_booking_requests_are_managed_in_admin(self):
        booking = EventBooking.objects.create(
            customer_name="Avery Jordan",
            email="avery@example.com",
            phone="555-0100",
            category=EventBooking.Category.MUSIC_CONCERT,
            event_date="2027-06-12",
            guest_count=120,
            venue="Garden Hall",
        )
        model_admin = admin.site._registry[EventBooking]
        self.assertIn("email", model_admin.search_fields)
        self.assertIn("status", model_admin.list_filter)

        user = get_user_model().objects.create_superuser(
            username="admin", email="admin@example.com", password="test-password"
        )
        self.client.force_login(user)
        response = self.client.get(reverse("admin:myapp_eventbooking_change", args=[booking.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Garden Hall")
