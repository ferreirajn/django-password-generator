from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.


def about(request):
    return render(request, 'generator/about.html')


def generator(request):
    return render(request, 'generator/generator.html')


def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    if request.GET.get('special'):
        characters.extend(list('.!@#$%^&*()_+'))

    length = int(request.GET.get('length', 12))
    the_password = ''

    for x in range(length):
        the_password += random.choice(characters)

    return render(request, 'generator/password.html', {'password': the_password})
