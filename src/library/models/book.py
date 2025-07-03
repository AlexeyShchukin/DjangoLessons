from enum import StrEnum

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

LAN_CHOICES = [
    ("en", "English"),
    ("fr", "French"),
    ("it", "Italian"),
]


class Genre(StrEnum):
    N_A = "N/A"
    FICTION = 'Fiction',
    NON_FICTION = 'Non-Fiction',
    SCIENCE_FICTION = 'Science Fiction',
    FANTASY = 'Fantasy',
    MYSTERY = 'Mystery',
    BIOGRAPHY = 'Biography'

    @classmethod
    def choices(cls):
        return [(attr.name, attr.value) for attr in cls]


class Book(models.Model):
    title = models.CharField(max_length=65)
    description = models.TextField(
        null=True,
        blank=True,
    )
    genre = models.CharField(
        max_length=50,
        choices=Genre.choices(),
        default=Genre.N_A,
    )
    pages = models.PositiveSmallIntegerField(
        validators=[MaxValueValidator(10000)],
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
