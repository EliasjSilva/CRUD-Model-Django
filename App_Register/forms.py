from django import forms
from . import models

GENDER = ()

class UserForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = '__all__'

        widgets = {
            # 'name': forms.TextInput(
            #     attrs={
            #         'placeholder': 'Enter your Full name',
            #         }
            #     ),
            'gender': forms.RadioSelect(
                attrs={
                    'type':'radio',
                    }
                ),
            'profession': forms.Select(
                attrs={
                    'placeholder': 'Your Profession',

                }
            ),
            'ocupation': forms.Select(
                attrs={
                    'placeholder': 'Your Ocupation',
                }
            ),
            # 'technologies': forms.CheckboxSelectMultiple(
            #     attrs={
            #         'class': 'checkbox',
            #     }
            # ),
            'date': forms.DateInput(
                format=('%d/%m/%Y'),
                attrs={
                    'placeholder': 'Select a date',
                    'type': 'date',
                }
            ),
            'email': forms.EmailInput(),
            'github': forms.TextInput(),
            'linkedin': forms.TextInput(),
        }