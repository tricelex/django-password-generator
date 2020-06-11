from django.http import HttpResponse
from django.shortcuts import render
import random


# Create your views here.
def home(request):
    return render(request, 'generator/home.html', {'password': 'sdhkhdsdvi334oasd'})


def password(request):
    the_password = ''
    characters = list('abcdefghijklmnopqrstuvwxyz')
    length = int(request.GET.get('length', 12))

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))
    for x in range(length):
        the_password += random.choice(characters)
    return render(request, 'generator/password.html', {'password': the_password})


def about(request):
    return render(request, 'generator/about.html', {'title': 'About Us'})
