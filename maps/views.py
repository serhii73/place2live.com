from rest_framework import generics

from maps.models import Country
from maps.serializers import CountrySerializer


class CountryListCreate(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
