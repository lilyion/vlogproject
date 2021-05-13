from django.db import models

# Create your models here.

class Vlog(models.Model):
    titlee = models.CharField(max_length=100)
    comment =  models.TextField()
    date = models.DateTimeField('date published')
