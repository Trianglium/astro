# Generated by Django 4.0.7 on 2022-11-13 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0008_tag_resource_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='astropoint',
            name='image_symbol',
            field=models.ImageField(blank=True, upload_to='learn/'),
        ),
    ]
