from django.shortcuts import render
import datetime


def home(request):
    date = datetime.datetime.now().date()
    name = 'Собакен'
    _contex = {'date': date, 'name': name}
    return render(request, 'home.html', _contex)
