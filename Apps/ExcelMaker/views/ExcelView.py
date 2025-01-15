from django.http import FileResponse
from Apps.ExcelMaker.ExcelLogic.ExcelGenerator import generar_xls_usuarios, generar_xlsx_tareas, generar_xlsx_proyectos, generar_xlsx_equipos

def descargar_xls_usuarios(request):
    return generar_xls_usuarios()

def descargar_xls_tareas(request):
    return generar_xlsx_tareas()

def descargar_xls_proyectos(request):
    return generar_xlsx_proyectos()

def descargar_xls_equipos(request):
    return generar_xlsx_equipos()