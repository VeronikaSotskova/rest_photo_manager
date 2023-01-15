from django.contrib.auth.models import User
from django.db import models


def upload_to_user_photo(instance, filename):
    return f"photos/{instance.user.id}/{filename}"


class Photo(models.Model):
    user = models.ForeignKey(
        to=User,
        verbose_name='Пользователь',
        related_name='photos',
        related_query_name='photos',
        on_delete=models.CASCADE,
    )

    file = models.ImageField(
        verbose_name='Фото',
        upload_to=upload_to_user_photo,
    )

    date_created = models.DateTimeField(
        verbose_name='Дата загрузки',
        auto_now_add=True,
    )

    x = models.FloatField(
        verbose_name='X координата геолокации',
        null=True,
        blank=True,
    )

    y = models.FloatField(
        verbose_name='Y координата геолокации',
        null=True,
        blank=True,
    )

    description = models.TextField(
        verbose_name='Описание',
        null=True,
        blank=True,
    )

    names = models.ManyToManyField(
        to='core.PhotoUser',
        verbose_name='Имена людей на фото',
        related_name='photos',
        related_query_name='photos',
        blank=True
    )

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото'
