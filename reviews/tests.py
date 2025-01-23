from django.test import TestCase, Client
from django.contrib.auth.models import User
from .models import ScoopReview, ReviewComment
from django.urls import reverse


class TestScoopReviewModel(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password")
        self.review = ScoopReview.objects.create(
            location="Test Location",
            blurb="A short description",
            slug="test-location",
            review="This is a test review.",
            rating=4.5,
            critic=self.user,
            status=1,
        )

    def test_review_creation(self):
        self.assertEqual(str(self.review), "Test Location | rated 4.5 by testuser")
        self.assertEqual(self.review.status, 1)


class TestReviewCommentModel(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password")
        self.review = ScoopReview.objects.create(
            location="Test Location",
            blurb="A short description",
            slug="test-location",
            review="This is a test review.",
            rating=4.5,
            critic=self.user,
            status=1,
        )
        self.comment = ReviewComment.objects.create(
            review=self.review,
            critic=self.user,
            comment="This is a test comment",
            accept=True,
        )

    def test_comment_creation(self):
        self.assertEqual(str(self.comment), "Comment This is a test comment by testuser")
        self.assertTrue(self.comment.accept)


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="testuser", password="password")
        self.review = ScoopReview.objects.create(
            location="Test Location",
            blurb="A short description",
            slug="test-location",
            review="This is a test review.",
            rating=4.5,
            critic=self.user,
            status=1,
        )

    def test_review_list_view(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "reviews/index.html")
        self.assertContains(response, "Test Location")

    def test_post_detail_view(self):
        response = self.client.get(reverse("review_detail", args=[self.review.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "reviews/post_detail.html")
        self.assertContains(response, "This is a test review.")

    def test_comment_creation_view(self):
        self.client.login(username="testuser", password="password")
        response = self.client.post(reverse("review_detail", args=[self.review.slug]), {
            "comment": "Test comment from view",
        })
        self.assertEqual(response.status_code, 302)  # Redirect after submission
        self.assertTrue(ReviewComment.objects.filter(comment="Test comment from view").exists())


class TestCommentPermissions(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password")
        self.other_user = User.objects.create_user(username="otheruser", password="password")
        self.review = ScoopReview.objects.create(
            location="Test Location",
            blurb="A short description",
            slug="test-location",
            review="This is a test review.",
            rating=4.5,
            critic=self.user,
            status=1,
        )
        self.comment = ReviewComment.objects.create(
            review=self.review,
            critic=self.user,
            comment="This is a test comment",
        )

    def test_delete_comment_permission(self):
        self.client.login(username="otheruser", password="password")
        response = self.client.get(reverse("comment_delete", args=[self.review.slug, self.comment.id]))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(ReviewComment.objects.filter(id=self.comment.id).exists())

        self.client.login(username="testuser", password="password")
        response = self.client.get(reverse("comment_delete", args=[self.review.slug, self.comment.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(ReviewComment.objects.filter(id=self.comment.id).exists())
