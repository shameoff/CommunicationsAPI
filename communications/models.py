from django.db import models


# Create your models here.
# Коммуникация (id, Дата, Балл, Пользователь, собеседник, мероприятие* (если было создано на мероприятии))


class Interlocutor(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, default=None)
    description = models.TextField(null=True)
    owner = models.ForeignKey('users.ExtendedUser', on_delete=models.CASCADE)

    def calculate_rating(self):
        pass


class Communication(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, default=None)
    description = models.TextField(null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)
    rate = models.IntegerField(null=False, blank=False, default=None)
    interlocutor = models.ForeignKey('communications.Interlocutor', default=None, on_delete=models.CASCADE)
