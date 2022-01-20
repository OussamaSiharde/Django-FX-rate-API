import json
from datetime import datetime

from django.core.management.base import BaseCommand

from exchange_core.rates.models import Currency, Rate


class Command(BaseCommand):
    help = "Load json data to database"

    def handle(self, *args, **kwargs):

        with open("fxrates_data.json") as f:
            rates = json.load(f)
            for rate in rates:
                currency, created = Currency.objects.get_or_create(name=rate["base"])
                name = rate["currency"]
                rate_date = datetime.strptime(
                    "{} {}".format(rate["date"], "01:00:00"), "%Y-%m-%d %H:%M:%S"
                )
                rate = rate["rate"]
                if not Rate.objects.filter(
                    name=name, rate_date__date=rate_date, rate=rate
                ).exists():
                    rate = Rate.objects.create(
                        name=name, rate_date=rate_date, rate=rate
                    )
                    currency.rates.add(rate)
