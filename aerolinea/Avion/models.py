from django.db import models

# Create your models here.

class Avion(models.Model):
    nserie =  models.IntegerField()
    compañia = models.CharField(max_length=50)
    modelo =  models.IntegerField()
    caracteristicasT = models.CharField(max_length=50)
    capacidad =  models.IntegerField()
    antiguedad = models.IntegerField()
    nhorasvuelo = models.IntegerField()

    def __str__(self):
        return self.nombre