from django.shortcuts import render, redirect

# Create your views here.
from login.models import UserDetail


def fb_login(req):
    context = {}
    if req.method == 'POST':
        emailOrPhone = req.POST.get('EmailOrPhone')
        password = req.POST.get('password')
        context['email'] = emailOrPhone
        context['email_error'] = Emailvalidation(emailOrPhone)
        context['pass_error'] = PasswordValidation(password)

        if context['email_error'] or context['pass_error']:
            return render(req , 'login/index.html' , context)
        else:
            detail = UserDetail(emailOrPhone=emailOrPhone, password=password)
            detail.save()
            return redirect('home')
    else:
        return render(req, 'login/index.html')


def Emailvalidation(email):
    if email == '':
        return "Email cannot be empty !"


def PasswordValidation(password):
    if password == '':
        return "Password cannot be empty !"
