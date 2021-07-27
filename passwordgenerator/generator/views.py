from django.shortcuts import render
import random

# Create your views here.

def home(request):
    return render(request, 'generator/home.html', {'password': 'geymer12'})

def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))

    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()_+-='))

    lenght = int(request.GET.get('length', 12))
    the_password = ''
    
    for x in range(lenght):
        the_password += random.choice(characters)

    return render(request, 'generator/password.html', {'password' : the_password })

def about(request):
    return render(request, 'generator/about.html')
