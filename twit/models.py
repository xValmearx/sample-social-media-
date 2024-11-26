from django.db import models
from django.conf import settings
from django.urls import reverse


class Twit(models.Model):
    """Twit model"""

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="twits")

    likes = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="liked_twits",
        blank=True,
    )

    body = models.TextField()

    image_url = models.CharField(max_length=300, blank=True)

    # image_url = ***** needs work

    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body

    def get_absolute_url(self):
        return reverse(
            "twit_list",
        )

    def get_like_url(self):
        """get like url based on PK"""
        return reverse("twit_like", kwargs={"pk": self.pk})


class Comment(models.Model):
    """Comment Model"""

    twit = models.ForeignKey(
        Twit,
        on_delete=models.CASCADE,
        related_name="comments",
    )
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="comments")
    body = models.CharField(max_length=140)

    def __str__(self):
        """string method"""
        return self.body

    def get_absolute_url(self):
        return reverse("twit_detail", kwargs={"pk": self.pk})
