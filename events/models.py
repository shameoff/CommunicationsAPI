from django.db import models


# Create your models here.
# Мероприятие (id, Название, Фото*, Описание*, Оценка, Список Коммуникаций, Дата)

class Event(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='events/images', blank=True)
    description = models.TextField()
    rating = models.IntegerField()
    communications = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
