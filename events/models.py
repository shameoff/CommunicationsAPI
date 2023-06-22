import uuid

from django.db import models


# Create your models here.
# Мероприятие (id, Название, Фото*, Описание*, Оценка, Список Коммуникаций, Дата)

class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    image_id = models.CharField(blank=True, null=True, max_length=100)
    description = models.TextField()
    rating = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
