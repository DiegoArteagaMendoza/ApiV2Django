# from django.urls import path
# from Apps.User.views.UserView import UserListPostView, UserDetailView

# urlpatterns = [
#     path('', UserListPostView.as_view(), name='user_list'),  # Ruta para listar y crear usuarios
#     path('<int:user_id>/', UserDetailView.as_view(), name='user_detail'),  # Ruta para detalles, actualización y eliminación de usuario
# ]


from django.urls import path
from Apps.User.views.UserView import UserListPostView, UserDetailView

urlpatterns = [
    path('list/', UserListPostView.as_view(), name='user_list'),  # Ruta para listar usuarios
    path('create/', UserListPostView.as_view(), name='user_create'),  # Ruta para crear usuarios
    path('details/<int:user_id>/', UserDetailView.as_view(), name='user_detail'),  # Ruta para detalles de usuario
    path('update/<int:user_id>/', UserDetailView.as_view(), name='user_update'),  # Ruta para actualizar usuarios
    path('delete/<int:user_id>/', UserDetailView.as_view(), name='user_delete'),  # Ruta para eliminar usuarios
]
