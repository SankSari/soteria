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

    # If the user is not a volunteer, this field will be filled
    # with the volunteer's username (incharge) of this user
    incharge = models.CharField(
        verbose_name='Incharge', null=True, blank=True, max_length=150)

    # Latitude and longitude (location of user)
    lat = models.CharField(
        verbose_name='Latitude', max_length=32, blank=True, null=True)
    lon = models.CharField(
        verbose_name='Longitude', max_length=32, blank=True, null=True)

    def __str__(self):
        return self.username
