from django import forms
from django.forms import MultiValueField, CharField, ChoiceField, MultiWidget, TextInput, Select
from datetime import  date , time,timedelta,datetime
from .models import *
from django.forms.extras.widgets import SelectDateWidget
import datetime
from datetime import date
from django.forms import widgets


#print(s)

class NameForm(forms.ModelForm):

    class Meta:

        model = Subscribers

        exclude = [""]

class DateForm(forms.ModelForm):


    class Meta:

        model = Rangdate

        exclude = [""]




class FormDate(forms.Form):

        try:

            start_d = Rangdate.objects.values_list('date_start', flat=True).last()
            end_d = Rangdate.objects.values_list('date_end', flat=True).last()
            print("Date start last", start_d)
            print("Date end last", end_d)
            # print(entry_list)
        except ObjectDoesNotExist:
            print("Either the entry or blog doesn't exist.")

        start_date = 1, " April ", 2017
        date_started = start_date[0]
        date_ended = 20
        # month = str(start_date[1])
        # year = str(start_date[2])
        try:

            e = Rangdate.objects.values_list('time_start', flat=True).last()
            u = Rangdate.objects.values_list('time_end', flat=True).last()
            print("Time start last", e)
            print("Time end last", u)
            # print(entry_list)
        except ObjectDoesNotExist:
            print("Either the entry or blog doesn't exist.")

        try:
            list_of_date_start = start_d.timetuple()[:3]
            year = list_of_date_start[0]
            month = list_of_date_start[1]
            day = list_of_date_start[2]
            print("Year=",year,"Month=",month,"Date=",day)
            list_of_date_end = end_d.timetuple()[:3]
            year_end = list_of_date_end[0]
            month_end = list_of_date_end[1]
            day_end = list_of_date_end[2]
            print(list_of_date_start)
            print(list_of_date_end)
            list_of_date = []
            for it in list_of_date:
                list_of_date[it] == list_of_date_start[it]

                print(it)
            print(list_of_date)
        except ObjectDoesNotExist:
            print("Either the entry or blog doesn't exist.")

        def gen(start, end,month, year):
             return ((str(i), str(i)+" "+str(month)+" "+str(year)) for i in range(start, end + 1))

        d = list(gen(day, day_end,month,year))

        print(d)

        def gen_time(start, end):
            return ((str(i), str(i) + "-" + str(i + 1)) for i in range(start, end + 1))

        t = list(gen_time(e, u))

        Choose_time = forms.ChoiceField(widget=forms.RadioSelect, choices=d)
        Choose_date = forms.ChoiceField(widget=forms.RadioSelect, choices=t )