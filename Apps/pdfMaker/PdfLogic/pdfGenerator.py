from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib import colors
from reportlab.lib.units import inch
from io import BytesIO
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from Apps.User.models.UserModel import User
from Apps.Projects.models.ProjectsModels import Project
from Apps.Tasks.models.TasksModels import Task

# Función para crear un buffer para almacenar el PDF
def crear_buffer():
    return BytesIO()

# Estilo para el título
estilo_titulo = TableStyle([
    ("FONTNAME", (0, 0), (-1, -1), "Times-Bold"),
    ("FONTSIZE", (0, 0), (-1, -1), 14),
    ("ALIGN", (0, 0), (-1, -1), "CENTER"),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 12),
])

# Estilo para la tabla
estilo_tabla = TableStyle([
    ("FONTNAME", (0, 0), (-1, 0), "Times-Bold"),
    ("FONTSIZE", (0, 0), (-1, 0), 12),
    ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
    ("ALIGN", (0, 0), (-1, 0), "CENTER"),
    ("BOTTOMPADDING", (0, 0), (-1, 0), 8),
    ("LEFTPADDING", (0, 0), (-1, -1), 6),  # Márgenes a la izquierda
    ("RIGHTPADDING", (0, 0), (-1, -1), 6),  # Márgenes a la derecha
    ("TOPPADDING", (0, 0), (-1, -1), 6),  # Márgenes arriba
    ("BOTTOMPADDING", (0, 0), (-1, -1), 6),  # Márgenes abajo
    ("FONTNAME", (0, 1), (-1, -1), "Times-Roman"),
    ("FONTSIZE", (0, 1), (-1, -1), 10),
    ("ALIGN", (0, 1), (-1, -1), "CENTER"),
    ("VALIGN", (0, 1), (-1, -1), "MIDDLE"),
    ("GRID", (0, 0), (-1, -1), 1, colors.black),
    ("BOX", (0, 0), (-1, -1), 2, colors.black),
])

# Crear el estilo para los párrafos
estilos = getSampleStyleSheet()
estilo_parrafo = ParagraphStyle(
    "Descripcion",
    parent=estilos["BodyText"],
    fontName="Times-Roman",
    fontSize=9,
    leading=10,
)

# Función para generar el PDF de usuarios
def generar_pdf_usuarios():
    buffer = crear_buffer()
    doc = SimpleDocTemplate(
        buffer,
        pagesize=letter,
        leftMargin=inch,
        rightMargin=inch,
        topMargin=inch,
        bottomMargin=inch,
    )

    elementos = []

    # Título
    titulo = [["Reporte de usuarios"]]
    tabla_titulo = Table(titulo, colWidths=[6.5 * inch])
    tabla_titulo.setStyle(estilo_titulo)
    elementos.append(tabla_titulo)

    # Encabezado de la tabla
    encabezado = ["Nombre completo", "RUT", "Email", "Teléfono", "Rol", "Estado"]
    datos = [encabezado]

    # Obtener los datos de los usuarios
    users = User.objects.all()
    for user in users:
        status = "Activo" if user.user_status == 1 else "No activo"
        datos.append([
            f"{user.user_name} {user.user_last_name}",
            user.user_rut,
            user.user_email,
            user.user_phone,
            user.user_role,
            status,
        ])

    # Crear la tabla
    tabla = Table(datos, colWidths=[1.5 * inch, 1.2 * inch, 2 * inch, 1 * inch, 1 * inch, 1 * inch])
    tabla.setStyle(estilo_tabla)
    elementos.append(tabla)

    # Construir el documento
    doc.build(elementos)
    buffer.seek(0)

    return buffer

# Función para generar el PDF de proyectos
def generar_pdf_proyectos():
    buffer = crear_buffer()
    doc = SimpleDocTemplate(
        buffer,
        pagesize=letter,
        leftMargin=inch,
        rightMargin=inch,
        topMargin=inch,
        bottomMargin=inch,
    )

    elementos = []

    # Título
    titulo = [["Reporte de proyectos"]]
    tabla_titulo = Table(titulo, colWidths=[6.5 * inch])
    tabla_titulo.setStyle(estilo_titulo)
    elementos.append(tabla_titulo)

    # Encabezado de la tabla
    encabezado = ["Nombre", "Descripción", "Inversión", "Fecha de inicio"]
    datos = [encabezado]

    # Obtener los datos de los proyectos
    projects = Project.objects.all()
    for project in projects:
        descripcion_parrafo = Paragraph(project.project_description, estilo_parrafo)
        datos.append([
            project.project_name,
            descripcion_parrafo,
            project.project_budget,
            project.project_start_date
        ])

    # Crear la tabla
    tabla = Table(datos, colWidths=[2 * inch, 2.5 * inch, 2 * inch, 1.5 * inch])
    tabla.setStyle(estilo_tabla)
    elementos.append(tabla)

    # Construir el documento
    doc.build(elementos)
    buffer.seek(0)

    return buffer

# Función para generar el PDF de tareas
def generar_pdf_tareas():
    buffer = crear_buffer()
    doc = SimpleDocTemplate(
        buffer,
        pagesize=letter,
        leftMargin=inch,
        rightMargin=inch,
        topMargin=inch,
        bottomMargin=inch,
    )

    elementos = []

    # Título
    titulo = [["Reporte de tareas"]]
    tabla_titulo = Table(titulo, colWidths=[6.5 * inch])
    tabla_titulo.setStyle(estilo_titulo)
    elementos.append(tabla_titulo)

    # Encabezado de la tabla
    encabezado = ["Tarea", "Descripción", "Usuario", "Proyecto", "Estado", "Equipo"]
    datos = [encabezado]

    # Obtener los datos de las tareas
    tasks = Task.objects.all()
    for task in tasks:
        descripcion_parrafo = Paragraph(task.task_description, estilo_parrafo)
        datos.append([
            task.task_name,
            descripcion_parrafo,
            task.task_user,
            task.task_project,
            task.task_status,
            task.task_team
        ])

    # Ajuste de los anchos de las columnas
    col_widths = [1.2 * inch, 2.0 * inch, 1.5 * inch, 1.5 * inch, 1.0 * inch, 1.2 * inch]

    # Crear la tabla
    tabla = Table(datos, colWidths=col_widths)
    tabla.setStyle(estilo_tabla)
    elementos.append(tabla)

    # Construir el documento
    doc.build(elementos)
    buffer.seek(0)

    return buffer
