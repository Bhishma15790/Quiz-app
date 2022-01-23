from dataclasses import field, fields
from django import forms
from django.contrib.auth.models import User
from django.forms import TextInput, EmailInput, Select, FileInput

from django.contrib.auth.forms import UserCreationForm



class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30,label= 'User Name :')
    email = forms.EmailField(max_length=200,label= 'Email :')
    fullname = forms.CharField(max_length=100, help_text='Full-Name',label= 'Full Name :')
    phoneno = forms.CharField(max_length=12, label='Phone No')

    class Meta:
        model = User
        fields = ('username', 'email', 'fullname', 'phoneno', 'password1', 'password2',)
    