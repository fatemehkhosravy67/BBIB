from django.db import models
from django.contrib.auth.models import AbstractUser

from django.utils.timezone import now


class DataEntry(models.Model):
    national_code = models.CharField(max_length=100)
    branch_code = models.CharField(max_length=100)
    value = models.IntegerField()
    created_time = models.DateTimeField(default=now, blank=True)


class CustomUser(AbstractUser):
    username = models.CharField(max_length=255, unique=True)
    branch_code = models.CharField(max_length=100)

    def __str__(self):
        return self.username
