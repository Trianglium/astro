# Generated by Django 4.0.7 on 2022-11-04 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("faq", "0004_astropoint"),
    ]

    operations = [
        migrations.CreateModel(
            name="Rule",
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
                ("title", models.CharField(max_length=200)),
                ("description", models.TextField(blank=True)),
            ],
        ),
    ]
