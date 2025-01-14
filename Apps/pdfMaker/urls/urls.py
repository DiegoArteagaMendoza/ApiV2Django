from django.urls import path
from Apps.pdfMaker.views.pdfView import descargar_pdf_usuarios, descargar_pdf_tareas, descargar_pdf_proyectos

urlpatterns = [
    path('usuarios/', descargar_pdf_usuarios, name='descargar_reporte_usuarios'),
    path('tareas/', descargar_pdf_tareas, name='descargar_reporte_tareas'),
    path('proyectos/', descargar_pdf_proyectos, name='descargar_reporte_proyectos')
]