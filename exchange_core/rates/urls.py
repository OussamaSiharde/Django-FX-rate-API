from django.conf.urls import include, url
from django.urls import path
from rest_framework.routers import DefaultRouter

from exchange_core.rates.rest.views import CurrencyViewSet

router = DefaultRouter()

app_name = "rates"

urlpatterns = [
    path("rates/<str:date>", CurrencyViewSet.as_view(), name="currency",),
]
