from django.shortcuts import render, redirect
from django.http import HttpResponse
from Apps.login.forms.loginForm import LoginForm
from Apps.User.models.UserModel import User
from django.contrib.auth.hashers import check_password

def login(request):
    title = 'Login'
    if request.method == 'GET':
        return render(request, 'login.html', {
            'title': title,
            'form': LoginForm()
        })
    else:
        userRut = request.POST.get('userRut')
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(user_rut=userRut)

            if user.user_status == 0:
                return HttpResponse("Usuario no activo")
    
            if user.user_password==password:
                return redirect('/user/list')
            else:
                return HttpResponse("Credenciales Incorrectas")
        except User.DoesNotExist:
            return HttpResponse("Usuario no encontrado")