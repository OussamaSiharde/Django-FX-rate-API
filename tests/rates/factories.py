import datetime

import factory
import factory.fuzzy

from django.utils import timezone

from exchange_core.rates.models import Currency, Rate


class CurrencyFactory(factory.DjangoModelFactory):
    class Meta:
        model = Currency


class RateFactory(factory.DjangoModelFactory):
    rate = factory.fuzzy.FuzzyDecimal(0.100, 3.500)
    rate_date = timezone.now()

    class Meta:
        model = Rate
