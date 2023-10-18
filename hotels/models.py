from django.db import models


class Hotels(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=50, verbose_name='Название отеля')
    location = models.CharField(max_length=70, verbose_name='Расположение')
    # stars = models.ForeignKey()
    price = models.PositiveIntegerField(max_length=10, verbose_name='Цена/чел.')
    existence = models.BooleanField(default=True, verbose_name='Наличие свободных мест')
    booked = models.BooleanField(default=True, verbose_name='Бронирование')
