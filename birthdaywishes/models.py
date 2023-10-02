from django.db import models
from django.db import models

class Persons(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    email=models.EmailField()

    def __str__(self):
        return self.name


# Create your models here.
