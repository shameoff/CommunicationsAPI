from django.db import models


# Create your models here.
# Коммуникация (id, Дата, Балл, Пользователь, собеседник, мероприятие* (если было создано на мероприятии))


class Communication(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    score = models.IntegerField()
    user = models.ForeignKey('users.ExtendedUser', on_delete=models.CASCADE, related_name='user')
    foreign_user = models.ForeignKey('users.ExtendedUser', on_delete=models.CASCADE, related_name='foreign_user')
    event = models.ForeignKey('events.Event', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.user} - {self.foreign_user}'
