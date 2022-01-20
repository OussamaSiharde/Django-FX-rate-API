from decimal import Decimal

import pytest
from factory import Faker
from rest_framework import status

from tests.rates.factories import RateFactory, CurrencyFactory


@pytest.mark.django_db
def test_rates_listing(client):
    rate = RateFactory.create(name=Faker("name"))
    currency = CurrencyFactory.create(name=Faker("name"))
    currency.rates.add(rate)

    response = client.get(
        "/api/rates/{}?base={}&symbols={}".format(
            str(rate.rate_date).split(".")[0].split(" ")[0], currency.name, rate.name
        ),
    )
    assert response.status_code == status.HTTP_200_OK
    assert round(Decimal(response.json()["Rates"][rate.name]), 2) == rate.rate
