# Generated by Django 5.1.1 on 2024-09-25 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0007_remove_band_limited_edition'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='limited_edition',
            field=models.BooleanField(default=False),
        ),
    ]