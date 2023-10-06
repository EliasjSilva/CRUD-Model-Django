from django.shortcuts import render, redirect

from . import models


def home(request):
    return render(request, 'register/home.html')


# Listing !! 
def liste(request):
    users = models.User.objects.all()
    return render(request, 'register/list.html', {'users':users})


# Creating !!
def form(request): 
    if request.method == 'POST':
    # Salvar os dados da tela para o banco de dados.

        # Person
        new_user = models.User()
        new_user.name = request.POST.get('name')
        new_user.photo = request.FILES.get('photo')
        new_user.date = request.POST.get('date')
        new_user.gender = request.POST.get('gender')

        # Status
        new_user.profession = request.POST.get('profession')
        new_user.ocupation = request.POST.get('ocupation')
        new_user.technologies = request.POST.getlist('technologies')
        new_user.experience = request.POST.get('experience')

        # Dados
        new_user.cpf = request.POST.get('cpf')
        new_user.phone = request.POST.get('phone')
        new_user.adress = request.POST.get('adress')
        new_user.locate = request.POST.get('locate')

        # Links
        new_user.email = request.POST.get('email')
        new_user.github = request.POST.get('github')
        new_user.linkedin = request.POST.get('linkedin')

        new_user.save()

        return redirect('home')
    else:
        return render(request, 'register/form.html')


# Reading
def user(request, id):
    user = models.User.objects.get(id=id)
    return render(request, 'register/user.html', {'user':user}) 