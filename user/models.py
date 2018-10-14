from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Core user for the app
    """

    # Add phone number
    phone_number = models.IntegerField(
        verbose_name='Phone Number',
        validators=[MaxValueValidator(
            9999999999), MinValueValidator(1000000000)],
        unique=True, blank=True, null=True)

    # Volunteer or not
    volunteer = models.BooleanField(verbose_name='Volunteer', default=False)

    def __str__(self):
        return self.username
