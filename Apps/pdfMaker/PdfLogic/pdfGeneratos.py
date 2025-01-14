from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib import colors
from reportlab.lib.units import inch
from io import BytesIO
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from Apps.User.models.UserModel import User
from Apps.Projects.models.ProjectsModels import Project
from Apps.Tasks.models.TasksModels import Task

# Crear un buffer para almacenar el PDF
buffer = BytesIO()

# Configuración del documento con márgenes
doc = SimpleDocTemplate(
    buffer,
    pagesize=letter,
    leftMargin=inch,
    rightMargin=inch,
    topMargin=inch,
    bottomMargin=inch,
)

estilo_titulo = TableStyle([
    ("FONTNAME", (0, 0), (-1, -1), "Times-Bold"),
    ("FONTSIZE", (0, 0), (-1, -1), 14),
    ("ALIGN", (0, 0), (-1, -1), "CENTER"),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 12),
])

# Aplicar estilo a la tabla
estilo_tabla = TableStyle([
    # Encabezado
    ("FONTNAME", (0, 0), (-1, 0), "Times-Bold"),
    ("FONTSIZE", (0, 0), (-1, 0), 12),
    ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
    ("ALIGN", (0, 0), (-1, 0), "CENTER"),
    ("BOTTOMPADDING", (0, 0), (-1, 0), 8),
    # Datos
    ("FONTNAME", (0, 1), (-1, -1), "Times-Roman"),
    ("FONTSIZE", (0, 1), (-1, -1), 10),
    ("ALIGN", (0, 1), (-1, -1), "CENTER"),
    ("VALIGN", (0, 1), (-1, -1), "MIDDLE"),
    # Líneas internas
    ("GRID", (0, 0), (-1, -1), 1, colors.black),
    # Borde exterior de la tabla
    ("BOX", (0, 0), (-1, -1), 2, colors.black),
])

# Crear el estilo para los párrafos
estilos = getSampleStyleSheet()
estilo_parrafo = ParagraphStyle(
    "Descripcion",
    parent=estilos["BodyText"],  # Utilizar el estilo de cuerpo de texto
    fontName="Times-Roman",  # Definir la fuente
    fontSize=10,  # Tamaño de la fuente
    leading=12,  # Espaciado entre líneas
)

def generar_pdf_usuarios():
    elementos = []

    # Título del reporte
    titulo = [["Reporte de usuarios"]]
    tabla_titulo = Table(titulo, colWidths=[6.5 * inch])  # Ajustar al ancho total disponible
    tabla_titulo.setStyle(estilo_titulo)
    elementos.append(tabla_titulo)

    # Encabezado de la tabla
    encabezado = ["Id", "Nombre completo", "RUT", "Email", "Teléfono", "Rol", "Estado"]
    datos = [encabezado]

    # Obtener los datos de los usuarios
    users = User.objects.all()
    for user in users:
        
        status = " "
        if user.user_status == 1:
            status = "Activo"
        else:
            status = "No activo"    
        
        datos.append([
            user.id,
            f"{user.user_name} {user.user_last_name}",
            user.user_rut,
            user.user_email,
            user.user_phone,
            user.user_role,
            status,
        ])

    # Crear la tabla con ancho ajustado al tamaño de la hoja
    tabla = Table(datos, colWidths=[0.5 * inch, 1.5 * inch, 1.2 * inch, 2 * inch, 1 * inch, 1 * inch, 1 * inch])


    tabla.setStyle(estilo_tabla)

    # Agregar la tabla al documento
    elementos.append(tabla)

    # Construir el documento
    doc.build(elementos)
    buffer.seek(0)

    return buffer

def generar_pdf_proyectos():   
    elementos = []
    
    titulo = [["Reporte de proyectos"]]
    tabla_titulo = Table(titulo, colWidths=[6.5 * inch])
    tabla_titulo.setStyle(estilo_titulo)
    elementos.append(tabla_titulo)
    
    encabezado = ["Id", "Nombre del proyecto", "Descripción del proyecto", "Inversión del proyecto", "Fecha de inicio"]
    datos = [encabezado]
        
    projects = Project.objects.all()
    for project in projects:
        # Convertir la descripción a un párrafo para saltos de línea automáticos
        descripcion_parrafo = Paragraph(project.project_description, estilo_parrafo)
        datos.append([
            project.id,
            project.project_name,
            descripcion_parrafo,  # Utilizar el párrafo con salto de línea automático
            project.project_budget,
            project.project_start_date
        ])
        
    tabla = Table(datos, colWidths=[0.5 * inch, 2 * inch, 2.5 * inch, 2 * inch, 1.5 * inch])

    tabla.setStyle(estilo_tabla)

    # Agregar la tabla al documento
    elementos.append(tabla)

    # Construir el documento
    doc.build(elementos)
    buffer.seek(0)

    return buffer

def generar_pdf_tareas():
    
    # Crear un buffer para almacenar el PDF
    buffer = BytesIO()

    # Configuración del documento con márgenes
    doc = SimpleDocTemplate(
        buffer,
        pagesize=letter,
        leftMargin=inch,
        rightMargin=inch,
        topMargin=inch,
        bottomMargin=inch,
    )

    estilo_titulo = TableStyle([
        ("FONTNAME", (0, 0), (-1, -1), "Times-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 14),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 12),
    ])

    # Aplicar estilo a la tabla
    estilo_tabla = TableStyle([
        # Encabezado
        ("FONTNAME", (0, 0), (-1, 0), "Times-Bold"),
        ("FONTSIZE", (0, 0), (-1, 0), 12),
        ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
        ("ALIGN", (0, 0), (-1, 0), "CENTER"),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 8),
        # Datos
        ("FONTNAME", (0, 1), (-1, -1), "Times-Roman"),
        ("FONTSIZE", (0, 1), (-1, -1), 10),
        ("ALIGN", (0, 1), (-1, -1), "CENTER"),
        ("VALIGN", (0, 1), (-1, -1), "MIDDLE"),
        # Líneas internas
        ("GRID", (0, 0), (-1, -1), 1, colors.black),
        # Borde exterior de la tabla
        ("BOX", (0, 0), (-1, -1), 2, colors.black),
    ])

    # Crear el estilo para los párrafos
    estilos = getSampleStyleSheet()
    estilo_parrafo = ParagraphStyle(
        "Descripcion",
        parent=estilos["BodyText"],  # Utilizar el estilo de cuerpo de texto
        fontName="Times-Roman",  # Definir la fuente
        fontSize=10,  # Tamaño de la fuente
        leading=12,  # Espaciado entre líneas
    )
    
    elementos = []
    
    titulo = [["Reporte de tareas"]]
    tabla_titulo = Table(titulo, colWidths=[6.5*inch])
    tabla_titulo.setStyle(estilo_titulo)
    elementos.append(tabla_titulo)
    
    encabezado = ["Id", "Tarea", "Descipción", "Usuario Asignado", "Proyecto Asignado", "Estado", "Equipo Asignado"]
    
    datos = [encabezado]
    
    tasks = Task.objects.all()
    for task in tasks:
        descripcion_parrafo = Paragraph(task.task_description, estilo_parrafo)
        datos.append([
            task.id,
            task.task_name,
            descripcion_parrafo,
            task.task_user,
            task.task_project,
            task.task_status,
            task.task_team
        ])
        
    tabla = Table(datos, colWidths=[0.5 * inch, 1.5 * inch, 2 * inch, 2 * inch, 1.5 * inch, 0.5 * inch, 1.5 * inch])
    
    tabla.setStyle(estilo_tabla)
    
    elementos.append(tabla)
    
    doc.build(elementos)
    buffer.seek(0)
    
    return buffer