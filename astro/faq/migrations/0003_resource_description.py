# Generated by Django 4.0.7 on 2022-11-03 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("faq", "0002_resource_image_resource_image_link"),
    ]

    operations = [
        migrations.AddField(
            model_name="resource",
            name="description",
            field=models.TextField(blank=True),
        ),
    ]