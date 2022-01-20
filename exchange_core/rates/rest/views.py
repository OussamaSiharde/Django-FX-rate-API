from datetime import datetime
import logging

from rest_framework import viewsets, mixins, parsers, renderers, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from exchange_core.rates.models import Currency

logger = logging.getLogger(__name__)


class CurrencyViewSet(APIView):
    """ CurrencyViewSet
    """

    parser_classes = (
        parsers.FormParser,
        parsers.MultiPartParser,
        parsers.JSONParser,
    )
    renderer_classes = (renderers.JSONRenderer,)
    permission_classes = [permissions.AllowAny]

    def get(self, request, date):
        """
        """
        rates = None
        rates_dict = {}

        base = request.GET.get('base')
        symbols = request.GET.get('symbols').split(',')
        currency_instance = Currency.objects.get(name=base)

        rates = currency_instance.rates.filter(name__in=symbols)

        formatted_date = datetime.strptime(
            "{} {}".format(date, "00:00:00"), "%Y-%m-%d %H:%M:%S"
        )
        if not rates.filter(rate_date = date).exists():
            closest_date = rates.filter(rate_date__lt = formatted_date)\
                .order_by('rate_date').first().rate_date
            rates = rates.filter(rate_date=closest_date)
        else:
            rates = rates.filter(rate_date=formatted_date)

        for rate in rates:
            rates_dict[rate.name] = rate.rate

        return Response(
            {
                "Base": base,
                "Date" : date,
                "Rates": rates_dict
            }
        )
