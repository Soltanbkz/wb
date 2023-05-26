from django.db import models
from django.utils import timezone
from functools import wraps

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=155)
    email = models.EmailField(blank=False)
    phone_number = models.CharField(max_length=15, blank=False)
    message = models.TextField(blank=False)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
