from django.db import models

LAN_CHOICES = [
    ("en", "English"),
    ("fr", "French"),
    ("it", "Italian"),
]


class Book(models.Model):
    title = models.CharField(max_length=65)
    description = models.TextField(
        null=True,
        blank=True,
    )
    language = models.CharField(
        max_length=20,
        choices=LAN_CHOICES,
        default=LAN_CHOICES[0][0],
    )
    published_date = models.DateField(
        auto_now_add=True,
    )

    def __str__(self):
        return f"{self.title} ({self.published_date})"