from django.http import FileResponse
from Apps.pdfMaker.PdfLogic.pdfGenerator import generar_pdf_usuarios, generar_pdf_tareas, generar_pdf_proyectos
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def descargar_pdf_usuarios(request):
    buffer = generar_pdf_usuarios()
    return FileResponse(buffer, as_attachment=True, filename='Reporte de usuarios.pdf')

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def descargar_pdf_proyectos(request):
    buffer = generar_pdf_proyectos()
    return FileResponse(buffer, as_attachment=True, filename='Reporte de proyectos.pdf')

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def descargar_pdf_tareas(request):
    buffer = generar_pdf_tareas()
    return FileResponse(buffer, as_attachment=True, filename='Reporte de tareas.pdf')