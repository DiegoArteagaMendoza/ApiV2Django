from django.urls import path
from Apps.User.views.UserView import UserListPostView, UserDetailView

urlpatterns = [
    path('', UserListPostView.as_view(), name='user_list'),  # Ruta para listar y crear usuarios
    path('<int:user_id>/', UserDetailView.as_view(), name='user_detail'),  # Ruta para detalles, actualización y eliminación de usuario
]
