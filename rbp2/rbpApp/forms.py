from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms



class SignUpForm(UserCreationForm):
    password2=forms.CharField(label = 'Confirm Password ( Again )', widget=forms.PasswordInput)
    domain_name=forms.CharField(label='Domain Name')
    class Meta:
        model=User
        fields = ['username','first_name','last_name','email','domain_name']
        labels = {'email':'Email'}
