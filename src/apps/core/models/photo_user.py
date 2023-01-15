from django.db import models


class PhotoUser(models.Model):
    name = models.CharField(
        verbose_name='Имя',
        max_length=255,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Имена людей на фото'
        verbose_name_plural = 'Имена людей на фото'
