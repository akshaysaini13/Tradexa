from django.db import models

# Create your models here.

from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=30)
    weight = models.IntegerField()
    price = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    