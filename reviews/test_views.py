from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .forms import CommentForm
from .models import ScoopReview


class TestScoopReviewViews(TestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            username="myUsername",
            password="myPassword",
            email="test@test.com"
        )
        self.post = ScoopReview(
            location="Reviews location",
            critic=self.user,
            slug="reviews-location",
            blurb="Reviews blurb",
            review="Reviews review",
            status=1
        )
        self.post.save()

    def test_render_post_detail_page_with_comment_form(self):
        response = self.client.get(
            reverse('post_detail', args=['reviews-location'])
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Reviews location", response.content)
        self.assertIn(b"Reviews review", response.content)
        self.assertIsInstance(
            response.context['comment_form'],
            CommentForm
        )
