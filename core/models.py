from statistics import mode
from django.db import models

# Create your models here.


class Equipo(models.Model):
    id_equipo= models.AutoField(primary_key=True)    
    name = models.CharField( max_length=50)
    direction = models.CharField(max_length=50)
    state = models.BooleanField(null=True)
    memory_free=models.IntegerField(null=True)
    pro_consum=models.IntegerField(null=True)



    def add(self):
            self.save


    def __str__(self):
            return self.name


