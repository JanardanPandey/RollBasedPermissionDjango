from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms



class SignUpForm(UserCreationForm):
    password2=forms.CharField(label = 'Confirm Password ( Again )', widget=forms.PasswordInput)
    class Meta:
        model=User
        fields = ['username','first_name','last_name','email']
        labels = {'email':'Email'}

from django.contrib.auth import authenticate
class UserLoginForm(forms.Form):
    domain = forms.CharField()
    project = forms.CharField()
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        domain = self.cleaned_data.get('domain')
        project = self.cleaned_data.get('project')
        

        if username and password:
            user = authenticate(username=username, password=password)
            if domain!='admin_domain':
                raise forms.ValidationError('Domain does not exist')
            if project not in ['admin','demo','test','test_project','peg']:
                raise forms.ValidationError('Project does not exist')
            if not user:
                raise forms.ValidationError('This user does not exist or incorrect password')
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect password')
            if not user.is_active:
                raise forms.ValidationError('This user is not active')
        return super(UserLoginForm, self).clean(*args, **kwargs)