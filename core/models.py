from django.db import models

# Create your models here.


class Equipo(models.Model):
    name = models.CharField( max_length=50)
    direction = models.CharField(max_length=50)
    state = models.BooleanField()


    def add(self):
            self.save


    def __str__(self):
            return self.name
