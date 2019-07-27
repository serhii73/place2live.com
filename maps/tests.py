from django.test import TestCase

from .models import Country


class CountryModelTests(TestCase):
    """Tests for post model."""

    def setUp(self):
        """Set up non-modifiable objects used by all test methods."""
        self.country = Country(
            name="Narnia",
            freedomhouse_score="15",
            quality_of_life_index="20",
            purchasing_power_index="",
            safety_index="2",
            health_care_index="10",
            cost_of_living_index="70",
            property_price_to_income_ratio="30",
            traffic_commute_time_index="20",
            pollution_index="5",
            climate_index="10",
        )

    def tearDown(self):
        """Clean-up test data."""
        del self.country

    def test_string_representation(self):
        """Test string representation country."""
        self.assertEqual(str(self.country), self.country.name)
