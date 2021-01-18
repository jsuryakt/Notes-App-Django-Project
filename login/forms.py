from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from login.models import Notes

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class notesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title','description','image']
        widgets = {
            'title': forms.TextInput(attrs={'class':'input form-control col-5 shadow p-3 mb-5 bg-white rounded'}),
            'description': forms.TextInput(attrs={'class':'input form-control form-control-lg col-8 shadow p-3 mb-5 bg-white rounded'}),
        }