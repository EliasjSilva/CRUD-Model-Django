from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import models, forms

@login_required
def home(request):
    return render(request, 'home.html')


# Listing !! 
@login_required
def liste(request):
    users = models.User.objects.all()
    return render(request, 'register/list.html', {'users':users})


# Creating !!
@login_required
def create(request):
    form = forms.UserForm(request.POST or None, request.FILES or None)
    
    if form.is_valid():
        form.save()
        return redirect('list')
    else:
        return render(request, 'register/form.html', {'form':form})

# Reading
@login_required
def read(request, id):
    user = models.User.objects.get(id=id)
    return render(request, 'register/user.html', {'user':user})


# Updating
@login_required
def update(request, id):
    edit = models.User.objects.get(id=id)
    form = forms.UserForm(request.POST or None, request.POST or None, instance=edit)

    if form.is_valid():
        form.save()
        return redirect('list')
    else:
        return render(request, 'register/form.html', {'form':form})


# Deleting
@login_required
def remove(request, id):
    remove = models.User.objects.get(id=id)
    remove.delete()
    return redirect('list')