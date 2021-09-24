from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm

from .forms import SignUpForm

# Create your views here.
#crete view function for signUP
def sign_up(request):
    if request.method == "POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Account Created Successfully..!!!')
            return HttpResponseRedirect('/login/')
    else:
        fm=SignUpForm()
    return render(request, 'enroll/signup.html',{'form':fm})

#Login View
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = AuthenticationForm(request=request, data = request.POST)
            if fm.is_valid():
                uname=fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username = uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request,"Login Successfully...!!!")
                    return HttpResponseRedirect('/profile/')
        else:
            fm = AuthenticationForm()
        return render(request, 'enroll/userlogin.html',{'forms':fm,'user':request.user})
    return HttpResponseRedirect('/profile/')
    


#user logout view
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

#user pass change with old password views
def user_change_pass(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = PasswordChangeForm(user=request.user, data=request.POST)
            if fm.is_valid():             
                fm.save()
                update_session_auth_hash(request,fm.user)
                messages.success(request, "password changed successfully...!!!!")
                return HttpResponseRedirect('/profile/')
        else:
            fm=PasswordChangeForm(user=request.user)
        return render(request, 'enroll/changepass.html',{'forms':fm})
    else:
        return HttpResponseRedirect('/login/')

#User password changing without old password
def user_change_password(request):
   if request.user.is_authenticated:
        if request.method == "POST":
            fm = SetPasswordForm(user=request.user, data=request.POST)
            if fm.is_valid():             
                fm.save()
                update_session_auth_hash(request,fm.user)
                messages.success(request, "password changed successfully...!!!!")
                return HttpResponseRedirect('/profile/')
        else:
            fm=SetPasswordForm(user=request.user)
        return render(request, 'enroll/changepass.html',{'forms':fm})
   else:
       return HttpResponseRedirect('/login/')

#Profile View
def user_profile(request):
    if request.user.is_authenticated:
        return render(request, 'enroll/profile.html')
    else:
        return HttpResponseRedirect('/login/')

from .forms import UserLoginForm
def login_view(request):
    if request.method == 'POST':
        fm = AuthenticationForm(request=request, data= request.POST)
        if fm.is_valid():
            print(fm.cleaned_data)
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)
                messages.success(request,"Login Successfully...!!!")
                # context = {'domain':domain,'project':project}
                return HttpResponseRedirect('/profile/')
    # if form.is_valid():
    #     username = form.cleaned_data.get('username')
    #     password = form.cleaned_data.get('password')
    #     domain = form.cleaned_data.get('domain')
    #     project = form.cleaned_data.get('project')
    #     user = authenticate(username=username, password=password)
    #     from dialog.common.login import Login
    #     l = Login()
    #     token = l.login(domain,project,username,password)
    #     request.session['projectname']=project
    #     request.session['auth_token'] = token.headers['X-Subject-Token']
    #     request.session['catalog'] = token.json()['token']['catalog']
    #     request.session['user'] = token.json()['token']['user']
    #     request.session['project'] = token.json()['token']['project']
    #     request.session['is_admin'] = token.json()['token']['is_admin_project']
    #     request.session['projectid']=token.json()['token']['project']['id']
        
    #     login(request, user)
    #     if next:
    #         return redirect(next)
    #     return redirect('/')
    fm = UserLoginForm()

    context = {
        'forms': fm,
    }
    return render(request, "enroll/userlogin.html", context)