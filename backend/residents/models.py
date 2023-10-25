from django.db import models
from django.contrib.auth.models import AbstractUser

SIGNALEMENT_STATUS = [
    ("en_attente", "En attente de traitement"),
    ("en_cours", "En cours de traitement"),
    ("traite", "Traité"),
]


class Resident(AbstractUser):
    first_name = models.CharField(max_length=50, blank=True)
    street = models.CharField(max_length=255)
    postal_number = models.IntegerField(blank=True)
    phone_number = models.CharField(max_length=10, unique=True, blank=True)
    born_date = models.DateField(blank=True)

    def __str__(self):
        return self.first_name


class Signalement(models.Model):
    emettor = models.ForeignKey(Resident, on_delete=models.CASCADE)
    posted_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    signalement_state = models.CharField(
        max_length=30, choices=SIGNALEMENT_STATUS, default="en_attente"
    )

    def __str__(self):
        return self.description[:50]
