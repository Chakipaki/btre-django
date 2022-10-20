from django.db import models
from django.utils import timezone


class Realtor(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    description = models.TextField(blank=True)
    email = models.CharField(default='', max_length=20)
    phone = models.CharField(default='', max_length=20)
    is_mvp = models.BooleanField(default=False)
    hire_date = models.DateTimeField(default=timezone.now(), blank=True)

    def __str__(self):
        return self.name
