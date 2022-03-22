from django.db import models
from django.utils import timezone

class Credentials(models.Model):
    login = models.CharField(max_length=1000)
    password = models.CharField(max_length=1000)
    created_date = models.DateTimeField(default=timezone.now)