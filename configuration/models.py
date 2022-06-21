from django.db import models

# Create your models here.
class Sysemail(models.Model):
    timemail = (
      (60, '1 hora'),
      (120, '2 horas'),
      (240, '3 horas'),
    )
    id_config = models.AutoField(primary_key=True)
    email  = models.CharField(max_length=100,null=True)
    passemail = models.CharField(max_length=100,null=True)
    recivedemail = models.CharField(max_length=100, null=True)
    subject = models.CharField(max_length=100, null=True)
    contentemail = models.CharField(max_length=200, null=True)
    time_mail= models.IntegerField(choices=timemail)
    
    
    
class Parameter(models.Model):
    time = (
    (5,   '5min'),
    (10, '10min'),
    (20, '20min'),
    (30, '30min'),
  )
    id_param=models.AutoField(primary_key=True)
    time_check= models.IntegerField(choices=time)
    
        