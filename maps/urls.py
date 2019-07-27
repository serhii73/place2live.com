from django.urls import path

from . import views


urlpatterns = [
    path('api/country/', views.CountryListCreate.as_view()),
]
