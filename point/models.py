from django.db import models

# Create your models here.
class score(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=20)
  job = models.CharField(max_length=10)
  dkp = models.IntegerField()
  ep = models.IntegerField()
  gp = models.IntegerField()


class record(models.Model):
  id = models.AutoField(primary_key=True)
  item = models.IntegerField(null=True,blank=True)
  dkp = models.IntegerField(null=True,blank=True)
  gp = models.IntegerField(null=True,blank=True)
  time = models.DateTimeField(null=True,blank=True)
  boss = models.CharField(max_length=40,blank=True)
  name = models.TextField(null=True,blank=True)
  ep = models.IntegerField(null=True,blank=True)

  