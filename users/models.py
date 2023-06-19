from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class ExtendedUser(AbstractUser):
    email = models.EmailField(null=False, blank=True)
