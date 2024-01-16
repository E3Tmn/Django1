from django.db import models

# Create your models here.
class Place(models.Model):
    title = models.CharField("Название", max_length=200)
    description_short = models.CharField("Краткое описание", max_length=250)
    description_long = models.TextField("Большое описание")
    long = models.DecimalField("Долгота", max_digits=17, decimal_places=14)
    lat = models.DecimalField("Широта", max_digits=17, decimal_places=14)

    def __str__(self):
        return self.title