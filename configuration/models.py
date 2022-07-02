from django.db import models

# Create your models here.
class Sysemail(models.Model):
    timemail = (
      (1800,'30 min'),
      (3600, '1 hora'),
      (7200, '2 horas'),
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
      (60, '1 min'),
     (120, '2 min'), 
    (300,   '5 min'),
    (600, '10 min'),
    (1200, '20 min'),
    (1800, '30 min'),
  )
    id_param=models.AutoField(primary_key=True)
    time_check= models.IntegerField(choices=time)
    
        