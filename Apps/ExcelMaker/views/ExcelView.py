from django.http import FileResponse
from rest_framework.decorators import api_view
from Apps.ExcelMaker.ExcelLogic.ExcelGenerator import generar_xls_usuarios, generar_xlsx_tareas, generar_xlsx_proyectos, generar_xlsx_equipos

@api_view(['GET', 'POST'])
def descargar_xls_usuarios(request):
    return generar_xls_usuarios()

@api_view(['GET', 'POST'])
def descargar_xls_tareas(request, fecha_inicio, fecha_fin):
    return generar_xlsx_tareas(fecha_inicio, fecha_fin)

@api_view(['GET', 'POST'])
def descargar_xls_proyectos(request, fecha_inicio, fecha_fin):
    return generar_xlsx_proyectos(fecha_inicio, fecha_fin)

@api_view(['GET', 'POST'])
def descargar_xls_equipos(request, fecha_inicio, fecha_fin):
    return generar_xlsx_equipos(fecha_inicio, fecha_fin)