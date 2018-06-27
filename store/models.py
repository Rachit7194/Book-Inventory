from django.db import models

# Create your models here.
from django.utils import timezone


class Book(models.Model):
    title = models.CharField(max_length=200)
    author  = models.CharField(max_length=200)
    description = models.TextField()
    publish_date = models.DateTimeField(default=timezone.now)
    price = models.DecimalField(default=0.00, decimal_places=2, max_digits=8)
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.title
