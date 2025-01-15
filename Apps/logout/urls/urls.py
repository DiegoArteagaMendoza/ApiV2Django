from django.urls import path
from Apps.logout.views.logoutView import logout

urlpatterns = [
    path('', logout, name='logout')
]