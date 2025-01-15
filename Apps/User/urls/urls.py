from django.urls import path
from Apps.User.views import UserView

urlpatterns = [   
    path('list/', UserView.ObtenerUsuarios, name='user_list'),  # Ruta para listar usuarios
    path('create/', UserView.CrearUsuario, name='user_create'),  # Ruta para crear usuarios
    path('details/<int:user_id>/', UserView.VerUsuario, name='user_detail'),  # Ruta para detalles de usuario
    path('update/<int:user_id>/', UserView.ActualizarUsuario, name='user_update'),  # Ruta para actualizar usuarios
    path('delete/<int:user_id>/', UserView.EliminarUsuario, name='user_delete'),  # Ruta para eliminar usuarios
]
