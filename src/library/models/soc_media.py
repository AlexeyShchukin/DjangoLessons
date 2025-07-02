from datetime import datetime

from django.db import models


class Post(models.Model):
    title: str = models.CharField(max_length=100)
    content: str = models.TextField(
        null=True,
        blank=True,
    )
    created_at: datetime = models.DateTimeField(auto_now_add=True)
    img_url = models.URLField(
        max_length=255,
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.title} ({self.created_at})"