# Generated by Django 4.2.2 on 2023-06-22 06:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='rating',
            field=models.IntegerField(default=None, validators=[django.core.validators.MinValueValidator(-2), django.core.validators.MaxValueValidator(2)]),
        ),
    ]
