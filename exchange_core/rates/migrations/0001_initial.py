# Generated by Django 3.1.6 on 2021-07-17 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Rate",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50, verbose_name="name")),
                ("rate_date", models.DateTimeField(verbose_name="Rate Date")),
                (
                    "rate",
                    models.DecimalField(decimal_places=8, default=0, max_digits=20),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created at"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated at"),
                ),
            ],
            options={
                "verbose_name": "rate",
                "verbose_name_plural": "rates",
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="Currency",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=50, unique=True, verbose_name="Name"),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created at"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated at"),
                ),
                (
                    "rates",
                    models.ManyToManyField(
                        blank=True, to="rates.Rate", verbose_name="Rates"
                    ),
                ),
            ],
            options={
                "verbose_name": "currency",
                "verbose_name_plural": "currencies",
                "ordering": ("name",),
            },
        ),
    ]
