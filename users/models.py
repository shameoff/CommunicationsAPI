from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class ExtendedUser(AbstractUser):
    description = models.TextField(null=True, blank=True)
    description2 = models.TextField(null=True, blank=True)
    # add additional fields in here

    def __str__(self):
        return self.username
