from django.urls import path
from Apps.User.views import UserView
from Apps.token.views.tokenView import ObtenerToken

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [   
    path('list/', UserView.ObtenerUsuarios, name='user_list'),  # Ruta para listar usuarios
    path('create/', UserView.CrearUsuario, name='user_create'),  # Ruta para crear usuarios
    path('details/<int:user_id>/', UserView.VerUsuario, name='user_detail'),  # Ruta para detalles de usuario
    path('update/<int:user_id>/', UserView.ActualizarUsuario, name='user_update'),  # Ruta para actualizar usuarios
    path('delete/<int:user_id>/', UserView.EliminarUsuario, name='user_delete'),  # Ruta para eliminar usuarios
    path('token/', ObtenerToken, name='obtener_token'), # Ruta para obtener el token del usuario
    path('profile/', UserView.PerfilUsuario, name='user_profile') # Ruta para el perfil de usuario
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)