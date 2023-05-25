from django.db import models

# Create your models here.

class puntosGPS(models.Model):
    latitud = models.FloatField()
    longitud = models.FloatField()

    def __str__(self):
        return str(self.latitud) + ", " + str(self.longitud) 