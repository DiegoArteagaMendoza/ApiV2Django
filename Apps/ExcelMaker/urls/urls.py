from django.urls import path
from Apps.ExcelMaker.views.ExcelView import descargar_xls_usuarios, descargar_xls_tareas, descargar_xls_proyectos, descargar_xls_equipos

urlpatterns = [
    path('usuarios/', descargar_xls_usuarios, name='descargar_xls_usuarios'),
    path('tareas/', descargar_xls_tareas, name='descargar_xls_tareas'),
    path('proyectos/', descargar_xls_proyectos, name='descargar_xls_proyectos'),
    path('equipos/', descargar_xls_equipos, name='descargar_xls_equipos')
]