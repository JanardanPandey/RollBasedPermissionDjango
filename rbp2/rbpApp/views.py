from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages


from .forms import SignUpForm

# Create your views here.
#crete view function for signUP
def sign_up(request):
    if request.method == "POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Account Created Successfully..!!!')
    else:
        fm=SignUpForm()
    return render(request, 'enroll/signup.html',{'form':fm})

#Login View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

def user_login(request):
    if request.method == "POST":
        fm = AuthenticationForm(request=request, data = request.POST)
        if fm.is_valid():
            uname=fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(username = uname, password=upass)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/profile/')
    else:
        fm = AuthenticationForm()
    return render(request, 'enroll/userlogin.html',{'forms':fm})


#Profile View
def user_profile(request):
    return render(request, 'enroll/profile.html')
