from django.conf import settings
from django.db import models


class Persons(models.Model):
    "Generated Model"
    firstName = models.TextField()
    lastName = models.CharField(
        max_length=256,
    )
    dateOfBirth = models.DateField()
    user = models.OneToOneField(
        "users.User",
        on_delete=models.CASCADE,
        related_name="persons_user",
    )
