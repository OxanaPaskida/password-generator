from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request, 'generator/home.html')

def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')

    specials = list('!@#$%^&*()_+')
    numberlist = list('123456789')

    uppercharacters = list('')
    for letter in characters:
        uppercharacters.append(letter.upper())

    length = int(request.GET.get('length', 12))

    if request.GET.get('uppercase'):
        characters.extend(uppercharacters)
        #characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(specials)
    if request.GET.get('numbers'):
        characters.extend(numberlist)

    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)
    return render(request, 'generator/password.html', {'password': thepassword})

def about(request):
    return render(request, 'generator/about.html')
