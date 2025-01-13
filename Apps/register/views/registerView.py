from django.shortcuts import render, redirect
from django.http import HttpResponse
from Apps.register.forms.registerForm import RegisterForm
from Apps.User.models.UserModel import User
from django.contrib.auth.hashers import make_password, check_password

def register(request):
    title = 'Register'
    if request.method == 'GET':
        return render(request, 'register.html', {
            'title': title, 
            'form': RegisterForm()
        })
    else:
        userName = request.POST.get('userName')
        userLastName = request.POST.get('userLastName')
        userRut = request.POST.get('userRut')
        userEmail = request.POST.get('userEmail')
        userPhone = request.POST.get('userPhone')
        userRole = request.POST.get('userRole')
        userPassword = request.POST.get('userPassword')
        userConfirmPassword = request.POST.get('userConfirmPassword')
        
        if userPassword != userConfirmPassword:
            return HttpResponse("Las contraseñas no coinciden")
            
        try:
            user = User.objects.create(
                user_name = userName,
                user_last_name = userLastName,
                user_email = userEmail,
                user_rut = userRut,
                user_phone = userPhone,
                user_password = userPassword,
                user_role = userRole,
                user_status = 1
            )
            return redirect('/user/list')
        except:
            return HttpResponse("Usuario no creado")    