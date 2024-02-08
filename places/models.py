from django.db import models

from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField("Название", max_length=200)
    description_short = models.CharField("Краткое описание", max_length=250)
    description_long = HTMLField("Большое описание")
    long = models.DecimalField("Долгота", max_digits=17, decimal_places=14)
    lat = models.DecimalField("Широта", max_digits=17, decimal_places=14)

    def __str__(self):
        return self.title


class Image(models.Model):
    place = models.ForeignKey(
        'Place',
        on_delete=models.CASCADE,
        null=True,
        related_name='images'
    )
    picture = models.ImageField("Картинка", blank=True, upload_to='media/')
    serial_number = models.PositiveIntegerField(
        "Порядковый номер",
        null=True,
        db_index=True
    )

    def __str__(self):
        return f'{self.id} - {self.place.title}'
