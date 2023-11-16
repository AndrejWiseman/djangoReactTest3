from django.db import models

# Create your models here.
class Film(models.Model):
    naziv = models.CharField(max_length=250)
    zanr = models.CharField(max_length=200)
    uloge = models.CharField(max_length=350)

    def __str__(self):
        return self.naziv

