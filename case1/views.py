from django.http import HttpResponse
from .forms import *
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
# Create your views here.
def test(request):
    name = "Udovenko"
    range_form = DateForm(request.POST or None)
    forma = NameForm(request.POST or None)
    date_chose = FormDate
    time_chose = FormTime


    ra={}
    if request.POST:
        print(request.POST)

        ra['date_start']=request.POST.get('date_start')
        ra['date_end'] = request.POST.get('date_start')
        ra['time_start'] = request.POST.get('date_start')
        ra['time_end'] = request.POST.get('date_start')
    if forma.is_valid():
        forma.save()

    return render(request, 'simple_task/home.html', locals(),{'ra':ra})

def post(self, request):
    range_form = DateForm(request.POST or None)
    if range_form.is_valid():
        range_form.save()

        return render(request, 'simple_task/home.html', {'form': range_form})


class MyView(FormView):
    form_class = DateForm
    template_name = 'home.html'
    success_url = '/test/'

    def form_valid(self, form):
        form.save()
        return super(MyView, self).form_valid(form)