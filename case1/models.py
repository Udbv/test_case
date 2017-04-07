from django.db import models

# Create your models here.


class Subscribers(models.Model):
    Full_name = models.CharField(max_length=128)
    email = models.EmailField()

    def __str__(self):

            return "Повне ім’я :'%s' Мило: '%s'" % (self.Full_name, self.email)


class Rangdate (models.Model):

    date_start = models.DateField(blank=True, default='07,04,2017', null=True)
    date_end = models.DateField(blank=True, default='12,04,2017', null=True)
    time_start = models.IntegerField(default=9)
    time_end = models.IntegerField(default=18)


    class Meta:
        order_with_respect_to = 'date_start'

    def __str__(self):

            return "Початок зустрічі :'%s' Година '%s' Кінець зустрічі:%s %s" % (self.date_start, self.time_start, self.date_end, self.time_end)

