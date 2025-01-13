from django.urls import path
from Apps.register.views.registerView import register

urlpatterns = [
    path('', register, name='register')
]