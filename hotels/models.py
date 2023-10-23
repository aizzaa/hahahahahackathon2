from django.db import models
from django_extensions.db.fields import AutoSlugField
from django.contrib.auth import get_user_model
from slugify import slugify
from review.models import Favorite, Comment


User = get_user_model()


class Category(models.Model):
    # USER_TYPE_CHOICE = [
    #     ('vip', 'VIP'),
    #     ('common', 'COMMON'),
    # ]
    title = models.CharField(max_length=10)
    slug = models.SlugField(max_length=50, unique=True, primary_key=True, blank=True)
    body = models.TextField(verbose_name='Описание')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save()

    def __str__(self):
        return self.title


class Hotels(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название отеля')
    location = models.CharField(max_length=70, verbose_name='Расположение')
    stars = models.ForeignKey(Favorite, on_delete=models.CASCADE, verbose_name='Рейтинг отеля')
    reviews = models.ForeignKey(Comment, on_delete=models.CASCADE, verbose_name='Отзывы')
    room_count = models.IntegerField(blank=True, default=10)
    def free_rooms(self):
        if cli
    # existence = models.BooleanField(default=True, verbose_name='Наличие свободных мест')
    # booked = models.BooleanField(default=True, verbose_name='Бронирование')
    # available_rooms =

    def __str__(self):
        return self.title


# common_category = Category(title='COMMON', slug='common', body='Описание для COMMON')
# common_category.save()


class Rooms(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название номера')
    slug = models.SlugField(max_length=30, primary_key=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='rooms', verbose_name='Категория')
    price = models.DecimalField(verbose_name='Цена/чел.', max_digits=10, decimal_places=2)
    descr = models.TextField(verbose_name='Описание комнаты')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

