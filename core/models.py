from pyexpat import model
from statistics import mode
from django.db import models
from django.forms import CharField

# Create your models here.


class Equipo(models.Model):
    id_equipo= models.AutoField(primary_key=True)    
    name = models.CharField( max_length=50)
    direction = models.CharField(max_length=50)
    pro_consum=models.CharField(null=True,max_length=500)
    memory_free=models.CharField(null=True,max_length=500)
    state = models.BooleanField(null=True)
    user_admin =models.CharField(null=True,max_length=100)
    passwordadmin= models.CharField(null=True,max_length=100)



    def add(self):
            self.save


    def __str__(self):
            return self.name
