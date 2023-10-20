#отзывы 

from django.db import models
from django.contrib.auth import get_user_model
from hotels.models import Hotels

User = get_user_model()


class Comment(models.Model):
    body = models.TextField()
    author = models.ForeignKey(
        User, related_name='comments',
        on_delete=models.CASCADE
    )
    hotel_comment = models.ForeignKey(
        Hotels,
        related_name='comments',
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)


class Rating(models.Model):
    raiting = models.PositiveSmallIntegerField()
    post = models.ForeignKey(
        User, related_name='raiting',
        on_delete=models.CASCADE,
    )
    author = models.ForeignKey(
        User, related_name='ratings',
        on_delete=models.CASCADE)
    