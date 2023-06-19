# Generated by Django 4.2.2 on 2023-06-19 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_extendeduser_description2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='extendeduser',
            name='description',
        ),
        migrations.RemoveField(
            model_name='extendeduser',
            name='description2',
        ),
        migrations.AlterField(
            model_name='extendeduser',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]