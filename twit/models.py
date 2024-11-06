from django.db import models
from django.conf import settings
from django.urls import reverse


class Twit(models.Model):
    """Twit model"""

    Author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="twits")

    body = models.TextField()

    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body

    # def get_absolute_url(self):
    #     return reverse("twit_details", kwargs={"pk": self.pk})


class Comment(models.Model):
    """Comment Model"""

    article = models.ForeignKey(
        Twit,
        on_delete=models.CASCADE,
        related_name="comments",
    )
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="comments")
    text = models.CharField(max_length=140)

    def __str__(self):
        """string method"""
        return self.text

    # def get_absolute_url(self):
    #     return reverse("")
