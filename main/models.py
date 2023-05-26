from django.db import models
from django.utils import timezone


class GeneralPage(models.Model):
    general_text = models.TextField(blank=True)
    general_photo = models.ImageField(upload_to='photos/')
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.general_text

    class Meta:
        verbose_name = 'Главная'
        verbose_name_plural = 'Главная'


class AboutText(models.Model):
    about_text = models.TextField(blank=True)
    about_photo = models.ImageField(upload_to='photos/')
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.about_text

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'


class Portfolio(models.Model):
    image = models.ImageField(upload_to='photos/')
    portfolio_text = models.TextField(blank=True)
    port_img = models.ImageField(upload_to='photos/')
    port_text = models.TextField(blank=True)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.portfolio_text

    class Meta:
        verbose_name = 'Портфолио'
        verbose_name_plural = 'Портфолио'


class Comments(models.Model):
    image = models.ImageField(upload_to='photos/')
    name = models.CharField(max_length=155)
    email = models.CharField(max_length=155)
    text = models.TextField(blank=True)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'