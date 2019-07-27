"""Models for Maps app."""
from django.db import models


class Country(models.Model):
    """Create Country model for Maps app."""

    name = models.CharField(max_length=200)
    freedomhouse_score = models.FloatField(blank=True, null=True)
    quality_of_life_index = models.FloatField(blank=True, null=True)
    purchasing_power_index = models.FloatField(blank=True, null=True)
    safety_index = models.FloatField(blank=True, null=True)
    health_care_index = models.FloatField(blank=True, null=True)
    cost_of_living_index = models.FloatField(blank=True, null=True)
    property_price_to_income_ratio = models.FloatField(blank=True, null=True)
    traffic_commute_time_index = models.FloatField(blank=True, null=True)
    pollution_index = models.FloatField(blank=True, null=True)
    climate_index = models.FloatField(blank=True, null=True)

    def __str__(self):
        """Return country name in admin."""
        return self.name
