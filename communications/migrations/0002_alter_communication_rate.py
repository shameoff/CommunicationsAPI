# Generated by Django 4.2.2 on 2023-06-21 23:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communications', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='communication',
            name='rate',
            field=models.IntegerField(default=None, validators=[django.core.validators.MinValueValidator(-2), django.core.validators.MaxValueValidator(2)]),
        ),
    ]
