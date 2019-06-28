from django.db import models

# Create your models here.
class Console(models.Model):
    name = models.CharField(max_length=30)
    brand = models.CharField(max_length=30)