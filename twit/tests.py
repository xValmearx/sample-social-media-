# Caleb Taylor
# CIS 218
# 11/28/2024

from django.test import TestCase

from django.contrib.auth import get_user_model

from django.urls import reverse

from .models import Twit, Comment


class ReviewTest(TestCase):
    """Test for the review the"""

    @classmethod
    def setUpTestData(cls):
        """setting up test user"""
        cls.user = get_user_model().objects.create_user(username="testuser", email="test@email.com", password="secret")

        cls.twit = Twit.objects.create(
            author=cls.user,
            body="Test Twit body",
            image_url="https://th.bing.com/th/id/OIP.B5egN0iHlkSonHQjG-mitQHaJp?w=164&h=213&c=7&r=0&o=5&dpr=1.1&pid=1.7",
        )

        cls.comment = Comment.objects.create(twit=cls.twit, author=cls.user, body="Test Comment body")

    def test_user_model(self):
        """Twit Testing"""
        self.assertEqual(self.twit.author.username, "testuser")
        self.assertEqual(self.twit.body, "Test Twit body")
        self.assertEqual(
            self.twit.image_url,
            "https://th.bing.com/th/id/OIP.B5egN0iHlkSonHQjG-mitQHaJp?w=164&h=213&c=7&r=0&o=5&dpr=1.1&pid=1.7",
        ),
        self.assertEqual(self.twit.get_absolute_url(), "/")

        """Comment Testing"""
        self.assertEqual(self.comment.twit.body, "Test Twit body")
        self.assertEqual(self.comment.author.username, "testuser")
        self.assertEqual(self.comment.body, "Test Comment body")
