from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    userpic = models.ImageField()
    email = models.EmailField(unique=True)
    phone = models.CharField(
        unique=True,
        blank=False,
        null=False,
        max_length=12
    )
    first_name = models.CharField(
        blank=False,
        null=False,
        max_length=50
    )
    last_name = models.CharField(
        blank=False,
        null=False,
        max_length=50
    )

    def __str__(self):
        return self.username