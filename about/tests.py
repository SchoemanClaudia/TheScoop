from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.messages import get_messages
from .models import About, CollaborateRequest
from .forms import CollaborateForm


class AboutModelTest(TestCase):
    def setUp(self):
        self.about = About.objects.create(
            name="John Doe",
            bio="A passionate developer.",
            avatar_image="placeholder"
        )

    def test_about_str_method(self):
        self.assertEqual(str(self.about), "John Doe")


class CollaborateRequestModelTest(TestCase):
    def setUp(self):
        self.collaborate_request = CollaborateRequest.objects.create(
            name="Jane Smith",
            email="jane@example.com",
            message="I'd love to collaborate!",
            read=False
        )

    def test_collaborate_request_str_method(self):
        self.assertEqual(
            str(self.collaborate_request),
            "Collaboration request from Jane Smith"
        )


class CollaborateFormTest(TestCase):
    def test_valid_form(self):
        form_data = {
            "name": "John Doe",
            "email": "john@example.com",
            "message": "Let's work together!"
        }
        form = CollaborateForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form_data = {
            "name": "",
            "email": "invalid-email",
            "message": ""
        }
        form = CollaborateForm(data=form_data)
        self.assertFalse(form.is_valid())


class MeetUsViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse("about")
        About.objects.create(
            name="John Doe",
            bio="A passionate developer.",
            avatar_image="placeholder"
        )

    def test_meet_us_get_request(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "about/meet_us.html")
        self.assertIn("about", response.context)
        self.assertIn("collaborate_form", response.context)

    def test_meet_us_post_request_valid_form(self):
        post_data = {
            "name": "Jane Smith",
            "email": "jane@example.com",
            "message": "I'd love to collaborate!"
        }
        response = self.client.post(self.url, data=post_data)
        self.assertEqual(response.status_code, 200)
        messages = [msg.message for msg in get_messages(response.wsgi_request)]
        self.assertIn("Your message was sent successfully.", messages)
        self.assertTrue(
            CollaborateRequest.objects.filter(
                email="jane@example.com").exists()
        )

    def test_meet_us_post_request_invalid_form(self):
        post_data = {
            "name": "",
            "email": "invalid-email",
            "message": ""
        }
        response = self.client.post(self.url, data=post_data)
        self.assertEqual(response.status_code, 200)
        messages = [msg.message for msg in get_messages(response.wsgi_request)]
        self.assertNotIn("Your message was sent successfully.", messages)
        self.assertFalse(CollaborateRequest.objects.exists())
