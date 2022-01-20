import pytest
from tests.rates.factories import CurrencyFactory, RateFactory
from factory import Faker


@pytest.mark.django_db
def test_currency():
    currency = CurrencyFactory.create(name=Faker("name"))
    assert currency.id


@pytest.mark.django_db
def test_rate():
    rate = RateFactory.create(name=Faker("name"))
    currency = CurrencyFactory.create(name=Faker("name"))
    currency.rates.add(rate)
    assert currency.id
