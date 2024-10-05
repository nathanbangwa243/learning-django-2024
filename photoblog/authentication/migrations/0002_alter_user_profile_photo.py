# Generated by Django 5.1.1 on 2024-10-05 22:12

import authentication.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_photo',
            field=models.ImageField(upload_to='', validators=[authentication.validators.ProfilePhotoValidator]),
        ),
    ]
