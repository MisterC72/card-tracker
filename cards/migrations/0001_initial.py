# Generated by Django 4.2.11 on 2024-03-26 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Card",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("provider", models.CharField(max_length=100)),
                ("limit", models.DecimalField(decimal_places=2, max_digits=10)),
                ("balance", models.DecimalField(decimal_places=2, max_digits=10)),
                ("is_zero_percent", models.BooleanField(default=False)),
                ("zero_percent_end", models.DateField(blank=True, null=True)),
            ],
        ),
    ]
