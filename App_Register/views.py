from django.shortcuts import render

from . import models


def home(request):
    return render(request, 'register/home.html')


# Listing !! 
def liste(request):
    users = models.User.objects.all()
    return render(request, 'register/list.html', {'users':users})


    
