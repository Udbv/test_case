from django import forms

from datetime import  date , time,timedelta,datetime
from .models import *
from django.forms import widgets
import datetime
start_date = datetime.date.today()
#start_time = datetime.now().hour
h=14
#time_list = [tuple(start_time + timedelta(hours=x) for x in range(0, h))]
TIME = (('1', '9-10',), ('2', '10-11',), ('3', '11-12',), ('4', '12-13',), ('5', '14-15',))

numdays = 3

date_list = [list(start_date + datetime.timedelta(days=x) for x in range(0, numdays))]


class NameForm(forms.ModelForm):

    class Meta:

        model = Subscribers

        exclude = [""]

class DateForm(forms.ModelForm):

    class Meta:

        model = Rangdate

        exclude = [""]

