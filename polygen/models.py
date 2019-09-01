from django.db import models

# class Polygon(models.Model):
#     name = models.CharField)(max_length = 30)
#     points = models.ManyToManyField(PolyPoints)

class PolyPoints(models.Model):
    _lat        = models.DecimalField(max_digits=19, decimal_places=9, null=True, blank=True)
    _long       = models.DecimalField(max_digits=19, decimal_places=9, null=True, blank=True)

class TwoPoints(models.Model):
    _lat        = models.DecimalField(max_digits=19, decimal_places=9, null=True, blank=True)
    _long       = models.DecimalField(max_digits=19, decimal_places=9, null=True, blank=True)
    _lat1       = models.DecimalField(max_digits=19, decimal_places=9, null=True, blank=True)
    _long1      = models.DecimalField(max_digits=19, decimal_places=9, null=True, blank=True)