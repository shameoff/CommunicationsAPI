import uuid

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


# Create your models here.
# Мероприятие (id, Название, Фото*, Описание*, Оценка, Список Коммуникаций, Дата)

class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    image_id = models.CharField(blank=True, null=True, max_length=100)
    description = models.TextField()
    rate = models.IntegerField(null=False, blank=False, default=None, validators=[MinValueValidator(-2), MaxValueValidator(2)])
    date = models.DateTimeField(auto_now_add=True)
