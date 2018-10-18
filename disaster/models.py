from django.db import models


class Disaster(models.Model):
    """Disaster model
    """

    # Keep the name lower-case always
    name = models.CharField(
        verbose_name='Name (Strictly Lowercase)', max_length=128)
    # How to know if event is this disaster
    symptoms = models.TextField(verbose_name='Symptoms')
    # Prevent any harm
    prevention = models.TextField(verbose_name='Prevention')

    def __str__(self):
        return self.name
