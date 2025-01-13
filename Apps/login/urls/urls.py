from django.urls import path
# from Apps.login.forms.loginForm import LoginForm
from Apps.login.views.loginView import login

urlpatterns = [
    path('', login, name='login')
]