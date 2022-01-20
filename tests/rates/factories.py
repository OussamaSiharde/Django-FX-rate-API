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
    rate_date = factory.fuzzy.FuzzyDateTime(
        timezone.now() + datetime.timedelta(days=1),
        timezone.now() + datetime.timedelta(days=10),
    )

    class Meta:
        model = Rate
