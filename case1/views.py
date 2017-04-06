
from .forms import *
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
# Create your views here.
def test(request):
    name = "UDovenko"
    range_form = DateForm(request.POST or None)
    forma = NameForm(request.POST or None)

    if request.method == 'POST':
        print(request.POST)
    return render(request, 'simple_task/home.html', locals())

def post(self, request):
    range_form = DateForm(request.POST or None)
    if range_form.is_valid():
        range_form.save()

        return render(request, 'simple_task/home.html', {'form': range_form})


class MyView(FormView):
    form_class = DateForm
    template_name = 'home.html'
    success_url = '/success/'

    def form_valid(self, form):
        form.save()
        return super(MyView, self).form_valid(form)