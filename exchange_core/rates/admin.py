from django.contrib import admin

from exchange_core.rates.models import Currency, Rate


class CurrencyAdmin(admin.ModelAdmin):
    """MovieAdmin
    """

    model = Currency
    list_display = ("name",)
    filter_horizontal = ("rates",)
    list_per_page = 15


class RateAdmin(admin.ModelAdmin):
    """PeopleAdmin
    """

    model = Rate
    list_display = ("name", "rate_date", "rate")
    list_per_page = 15


admin.site.register(Currency, CurrencyAdmin)
admin.site.register(Rate, RateAdmin)
