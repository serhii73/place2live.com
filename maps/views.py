from django.shortcuts import render

from .models import Country


def show_map(request):
    countries = Country.objects.all()
    return render(request, 'maps/index.html', {'countries': countries})
