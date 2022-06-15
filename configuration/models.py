from django.db import models

# Create your models here.
class Sysemail(models.Model):
    id_config = models.AutoField(primary_key=True)
    email  = models.CharField(max_length=100,null=True)
    passemail = models.CharField(max_length=100,null=True)
    recivedemail = models.CharField(max_length=100, null=True)
    subject = models.CharField(max_length=100, null=True)
    contentemail = models.CharField(max_length=200, null=True)
    
    
    
class Parameters(models.Model):
    time = (
    (10, '10min'),
    (20, '20min'),
    (30, '30min'),
  )
    time_check= models.IntegerField(choices=time)
        