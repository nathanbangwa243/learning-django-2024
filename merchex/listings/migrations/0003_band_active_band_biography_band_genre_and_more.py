# Generated by Django 5.1.1 on 2024-09-25 14:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_listing'),
    ]

    operations = [
        migrations.AddField(
            model_name='band',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='band',
            name='biography',
            field=models.CharField(default='Enter a bio', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='band',
            name='genre',
            field=models.CharField(choices=[('HH', 'Hip Hop'), ('SP', 'Synth Pop'), ('AR', 'Alternative Rock'), ('GP', 'Gospel'), ('SL', 'Slow')], default='GP', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='band',
            name='official_homepage',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='band',
            name='year_formed',
            field=models.IntegerField(default=2010, validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2024)]),
            preserve_default=False,
        ),
    ]
