# Generated by Django 4.2.2 on 2023-06-21 16:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Interlocutor',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(default=None, max_length=100)),
                ('description', models.TextField(null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Communication',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(default=None, max_length=100)),
                ('description', models.TextField(null=True)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('rate', models.IntegerField(default=None)),
                ('interlocutor', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='communications.interlocutor')),
            ],
        ),
    ]
