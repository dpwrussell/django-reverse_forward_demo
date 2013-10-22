from django.db import models

# Cars
class Car(models.Model):
    name = models.CharField(max_length=32)

    def parts_with_manufacturers(self):
        return self.part_set.select_related('manufacturer')

# Manufacturers
class Manufacturer(models.Model):
    name = models.CharField(max_length=32)

# Parts
class Part(models.Model):
    name = models.CharField(max_length=32)
    car = models.ForeignKey(Car)
    manufacturer = models.ForeignKey(Manufacturer)
