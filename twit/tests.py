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

    def test_login(self):
        # Log in the test user
        login = self.client.login(username="testuser", password="secret")
        self.assertTrue(login)

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

    def test_twit_list_page(self):
        """test for the Main page or the list view of all the twits"""

        # Test user must me logged in or else my template will redirect them to the login page
        login = self.client.login(username="testuser", password="secret")

        # get the root of the page
        response = self.client.get(reverse("home"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "twit_list.html")
        self.assertContains(response, "Test Twit body")
        self.assertContains(response, "Test Comment body")

    def test_public_profile(self):

        # get public profile page
        response = self.client.get(reverse("public_profile", kwargs={"pk": 1}))

        # checks of the page is found
        self.assertEqual(response.status_code, 200)

        # checks the templates being used
        self.assertTemplateUsed("public_profile.html")

        # checks for the user name
        self.assertContains(response, "testuser")

        # checks for the email
        self.assertContains(response, "test@email.com")

    def test_private_profile(self):
        """Test the user private profile"""

        # Test user must me logged in, private page can only be acessed to the user itself
        login = self.client.login(username="testuser", password="secret")

        # get public profile page
        response = self.client.get(reverse("profile", kwargs={"pk": 1}))

        # checks of the page is found
        self.assertEqual(response.status_code, 200)

        # checks the templates being used
        self.assertTemplateUsed("profile.html")

        # checks for the user name
        self.assertContains(response, "testuser")
