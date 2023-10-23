# отзывы

from django.db import models
from django.contrib.auth import get_user_model
from hotels.models import Hotels
from django.core.validators import MaxValueValidator, MinValueValidator

User = get_user_model()


class Comment(models.Model):
    body = models.TextField()
    author = models.ForeignKey(
        User, related_name='comments',
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(auto_now_add=True)


class Rating(models.Model):
    rating = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)],
        blank=True,
        default=0
    )

    author = models.ForeignKey(
        User, related_name='rating',
        on_delete=models.CASCADE)

    hotel = models.ForeignKey(
        Hotels, related_name='rating',
        on_delete=models.CASCADE,
    )

class Likes(models.Model):
    customer = models.ForeignKey(
            User, related_name='likes',
            on_delete=models.CASCADE,
            verbose_name='Поставил лайк',
            null=True,

        )

    liked_hotel = models.ForeignKey(
            Hotels, related_name='likes',
            on_delete=models.CASCADE
        )

    like = models.BooleanField(
            default=False
        )
    liked_at = models.DateTimeField(
            auto_now_add=True
        )

class Favorite(models.Model):  # добавление в избранные отели

    customer = models.ForeignKey(
            User, related_name='favorite',
            on_delete=models.CASCADE,
            null=True
        )

    favorite_hotel = models.ForeignKey(
            Hotels, related_name='favorite',
            on_delete=models.CASCADE
        )

    created_at = models.DateField(
            auto_now_add=True
        )