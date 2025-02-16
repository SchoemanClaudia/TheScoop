from django.test import TestCase
from django.urls import reverse
from .models import About
from .forms import CollaborateForm


class TestAboutView(TestCase):
    """
    Tests for the About view
    """

    def setUp(self):
        """
        Creates about me content
        """
        self.about_content = About(
            name="About Me", bio="This is about me."
        )
        self.about_content.save()

    def test_render_about_page_with_collaborate_form(self):
        """
        Verifies get request for about me containing a collaboration form
        """
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'About Me', response.content)
        self.assertIsInstance(
            response.context['collaborate_form'], CollaborateForm
        )

    def test_successful_collaboration_request_submission(self):
        """
        Test for a user requesting a collaboration
        """
        form_data = {
            "name": "Test User",
            "email": "test@example.com",
            "message": "This is a test message.",
        }
        response = self.client.post(reverse('about'), form_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Your message was sent successfully.', response.content
        )
