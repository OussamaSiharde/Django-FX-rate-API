from django.urls import include, path

urlpatterns = [
    path("", include("exchange_core.rates.urls")),
]
