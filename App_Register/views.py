from django.shortcuts import render, redirect

from . import models

from . import forms


def home(request):
    return render(request, 'register/home.html')


# Listing !! 
def liste(request):
    users = models.User.objects.all()
    return render(request, 'register/list.html', {'users':users})


# Creating !!
def create(request):
    form = forms.UserForm(request.POST or None, request.FILES)
    
    if form.is_valid():
        form.save()
        return redirect('list')
    else:
        return render(request, 'register/form.html', {'form':form})

# Reading
def read(request, id):
    user = models.User.objects.get(id=id)
    return render(request, 'register/user.html', {'user':user})


# Updating
def update(request, id):
    edit = models.User.objects.get(id=id)
    form = forms.UserForm(request.POST or None, request.FILES, instance= edit)

    if form.is_valid():
        form.save()
        return redirect('list')
    else:
        return render(request, 'register/form.html', {'form':form})


# Deleting
def remove(request, id):
    remove = models.User.objects.get(id=id)
    remove.delete()
    return redirect('list')