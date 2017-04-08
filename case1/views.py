from django.http import HttpResponseRedirect
from .forms import *
from .models import *
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.contrib.auth.decorators import login_required
# Create your views here.


def test(request):

    range_form = DateForm(request.POST or None)
    form_class = FormDate
    forma = NameForm(request.POST or None)

    if request.POST:
        print(request.POST)

    if range_form.is_valid():
        range_form.save()
        return HttpResponseRedirect('range/')
    return render(request, 'simple_task/home.html', locals())


def post(self, request):
    forma = NameForm(request.POST or None)
    if forma.is_valid():
        forma.save()
    return render(request, 'simple_task/name_form.html', locals(),)

@login_required
class MyView(FormView):


    form_class = FormDate
    template_name = 'simple_task/name_form.html'
    success_url = '/tested/'

    def form_valid(self, form):
        form.save()
        return super(MyView, self).form_valid(form)