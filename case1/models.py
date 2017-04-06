from django.db import models

# Create your models here.


class Subscribers(models.Model):
    Full_name = models.CharField(max_length=128)
    email = models.EmailField()




class Rangdate (models.Model):
    date_start = models.DateField(blank=True, default='<jamming-date>', null=True)
    date_end = models.DateField(blank=True, default='<jamming-date>', null=True)
    time_start = models.IntegerField(default=9)
    time_end = models.IntegerField(default=10)