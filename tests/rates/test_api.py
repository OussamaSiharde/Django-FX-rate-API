import pytest
from factory import Faker
from rest_framework import status

from django.urls import reverse

from tests.rates.factories import RateFactory, CurrencyFactory


@pytest.mark.django_db
def test_movies_listing(client):
    rate = RateFactory.create(name=Faker("name"))
    currency = CurrencyFactory.create(name=Faker("name"))
    currency.rates.add(rate)
