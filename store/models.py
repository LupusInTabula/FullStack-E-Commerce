from django.db import models


# Create your models here.

class Store(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=20)
    description = models.TextField()
    price = models.FloatField()
    stock = models.IntegerField()

    def __str__(self):
        return self.name


class Meta:
    ordering = ['name']
