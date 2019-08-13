"""Models for Maps app."""
from django.db import models


class Country(models.Model):
    """Create Country model for Maps app."""

    name = models.CharField(max_length=200)
    population = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        """Return country name in admin."""
        return self.name
