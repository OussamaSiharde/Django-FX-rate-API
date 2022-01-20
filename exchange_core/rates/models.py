from django.db import models
from django.utils.translation import ugettext_lazy as _


class Currency(models.Model):
    """
        Currency
    """

    name = models.CharField(_("Name"), max_length=50, unique=True)

    rates = models.ManyToManyField("Rate", verbose_name=_("Rates"), blank=True)

    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)

    class Meta:
        ordering = ("name",)
        verbose_name = "currency"
        verbose_name_plural = "currencies"

    def __str__(self):
        return "{}".format(self.name)


class Rate(models.Model):
    """
        Rate
    """

    name = models.CharField(_("name"), max_length=50)
    rate_date = models.DateTimeField(_("Rate Date"))
    rate = models.DecimalField(max_digits=20, decimal_places=8, default=0)

    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)

    class Meta:
        ordering = ("name",)
        verbose_name = "rate"
        verbose_name_plural = "rates"

    def __str__(self):
        return "{}".format(self.name)
