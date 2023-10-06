from django.contrib import admin

from . import models

@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_filter = ['gender', 'profession', 'ocupation']
    search_fields = ['name']
    list_display = ['name', 'photo', 'gender', 'date', 'profession', 'ocupation', 'technologies', 'experience', 'cpf', 'phone', 'adress', 'locate', 'email', 'github', 'linkedin']
    list_per_page = 8

    # # Change the select option to RADIO Button
    radio_fields = {'profession':admin.HORIZONTAL, 'gender':admin.HORIZONTAL, 'ocupation':admin.HORIZONTAL}