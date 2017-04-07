from django import forms
from django.forms import MultiValueField, CharField, ChoiceField, MultiWidget, TextInput, Select
from datetime import  date , time,timedelta,datetime
from .models import *
from django.forms.extras.widgets import SelectDateWidget
import datetime
from datetime import date
from django.forms import widgets
start_date = 10," April ",2017
time_start = 4
time_end = 10
class NameForm(forms.ModelForm):

    class Meta:

        model = Subscribers

        exclude = [""]

class DateForm(forms.ModelForm):

    class Meta:

        model = Rangdate

        exclude = [""]

    def gen_time(start, end):
        return ((str(i), str(i)+"-"+str(i+1)) for i in range(start, end + 1))

    t = list(gen_time(time_start, time_end))
    TIME = (('1', '9-10',), ('2', '10-11',), ('3', '11-12',), ('4', '12-13',), ('5', '14-15',))
    Choose_time = forms.ChoiceField(widget=forms.RadioSelect, choices=t)

    date_start = start_date[0]
    date_end = 20
    month = str(start_date[1])
    year = str(start_date[2])

    def gen(start, end, month, year):
        return ((str(i), str(i) + month + year) for i in range(start, end + 1))

    d = list(gen(date_start, date_end, month, year))

    Choose_date = forms.ChoiceField(widget=forms.RadioSelect, choices=d, )
#class FormTime(forms.Form):




#class FormDate(forms.Form):

