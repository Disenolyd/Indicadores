# Importaciones principales de Django y librerías externas
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import JsonResponse, FileResponse
from .models import Indicador, Meta
import io
from django.conf import settings
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import ImageReader
import matplotlib.pyplot as plt
import tempfile
from datetime import datetime
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Spacer
from reportlab.lib.units import mm
from reportlab.platypus import Frame
from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import IndicadorSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes

# Lista de correos permitidos para acceder al sistema
ALLOWED_EMAILS = [
    'juan.alvarez@design.com.co',
    'sofia.garcia@design.com.co',
    'andres.guzman@design.com.co',
    'vamos.design@gmail.com',
]

# Vista personalizada de login
# Valida usuario y contraseña, y restringe acceso a correos permitidos
# Redirige a home si el login es exitoso
# Muestra mensajes de error si el usuario no está autorizado o la contraseña es incorrecta

def custom_login(request):
    if request.method == 'POST':
        email = request.POST.get('username')
        password = request.POST.get('password')
        if email not in ALLOWED_EMAILS:
            messages.error(request, 'Correo no autorizado. Por favor, contacte al administrador.')
            return render(request, 'sig/login.html')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Contraseña incorrecta o usuario no existe. Si olvidó su contraseña, contacte al administrador.')
    return render(request, 'sig/login.html')

# Vista principal protegida por login
# Si no hay submenú seleccionado, redirige a home (el frontend muestra estrategica1 por defecto)
# Si ya hay submenú, renderiza la página principal con el usuario y el submenú seleccionado

@login_required
def home(request):
    # Renderiza la página principal, aunque no haya submenú seleccionado
    submenu_seleccionado = request.session.get('submenu_seleccionado')
    return render(request, 'sig/home.html', {
        'user': request.user,
        'submenu_seleccionado': submenu_seleccionado
    })

# Vista para cerrar sesión y redirigir al login

def custom_logout(request):
    logout(request)
    return redirect('login')

# --- API REST para indicadores estándar (mensual, trimestral, semestral) ---
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def indicadores_api(request, submenu):
    # Filtra los indicadores por submenú y los ordena por periodo y mes
    indicadores = Indicador.objects.filter(submenu=submenu).order_by('periodo', 'mes')
    data = list(indicadores.values())
    meta = None
    # Obtiene la meta dinámica desde la base de datos
    try:
        meta_obj = Meta.objects.get(submenu=submenu)
        meta = {
            "valor": meta_obj.valor,
            "tipo": meta_obj.tipo,
            "descripcion": meta_obj.descripcion
        }
    except Meta.DoesNotExist:
        meta = None
    # Lógica personalizada para calcular porcentajes según el submenú
    # (Ejemplo: TIC, Operaciones, etc.)
    if submenu == 'tic1':
        for d in data:
            d['tickets_cerrados'] = d.get('tickets_cerrados') or 0
            d['tickets_abiertos_hardware'] = d.get('tickets_abiertos_hardware') or 0
            d['tickets_abiertos_software'] = d.get('tickets_abiertos_software') or 0
            total = d['tickets_cerrados'] + d['tickets_abiertos_hardware'] + d['tickets_abiertos_software']
            d['porcentaje'] = round((d['tickets_cerrados'] / total) * 100) if total > 0 else 0
    elif submenu == 'tic2':
        for d in data:
            d['total_copias_seguridad_exitosa'] = d.get('total_copias_seguridad_exitosa') or 0
            d['total_copias_realizadas'] = d.get('total_copias_realizadas') or 0
            total = d['total_copias_realizadas']
            exitosas = d['total_copias_seguridad_exitosa']
            d['porcentaje'] = round((exitosas / total) * 100) if total > 0 else 0
    elif submenu == 'tic3':
        for d in data:
            d['ataques_ciberseguridad'] = d.get('ataques_ciberseguridad') or 0
            d['total_equipos'] = d.get('total_equipos') or 0
            total = d['total_equipos']
            ataques = d['ataques_ciberseguridad']
            d['porcentaje'] = round((ataques / total) * 100) if total > 0 else 0
    elif submenu == 'tic4':
        for d in data:
            d['mantenimientos_programados'] = d.get('mantenimientos_programados') or 0
            d['total_mantenimientos_realizados'] = d.get('total_mantenimientos_realizados') or 0
            total = d['mantenimientos_programados']
            realizados = d['total_mantenimientos_realizados']
            d['porcentaje'] = round((realizados / total) * 100) if total > 0 else 0
    elif submenu == 'operaciones1':
        for d in data:
            d['num_no_utilizadas'] = d.get('num_no_utilizadas') or 0
            d['total_disponibles'] = d.get('total_disponibles') or 0
            total = d['total_disponibles']
            no_utilizadas = d['num_no_utilizadas']
            d['porcentaje'] = round((no_utilizadas / total) * 100) if total > 0 else 0
    elif submenu == 'operaciones2':
        for d in data:
            d['num_sin_novedad'] = d.get('num_sin_novedad') or 0
            d['total_inspecciones_realizadas'] = d.get('total_inspecciones_realizadas') or 0
            total = d['total_inspecciones_realizadas']
            sin_novedad = d['num_sin_novedad']
            d['porcentaje'] = round((sin_novedad / total) * 100) if total > 0 else 0
    elif submenu == 'operaciones3':
        for d in data:
            d['sum_no_retorno'] = d.get('sum_no_retorno') or 0
            d['sum_total_documentos'] = d.get('sum_total_documentos') or 0
            total = d['sum_total_documentos']
            no_retorno = d['sum_no_retorno']
            d['porcentaje'] = round((no_retorno / total) * 100) if total > 0 else 0
    elif submenu == 'operaciones4':
        for d in data:
            d['num_entregados_tiempo'] = d.get('num_entregados_tiempo') or 0
            d['total_servicios_prestados'] = d.get('total_servicios_prestados') or 0
            total = d['total_servicios_prestados']
            entregados = d['num_entregados_tiempo']
            d['porcentaje'] = round((entregados / total) * 100) if total > 0 else 0
    elif submenu == 'operaciones5':
        for d in data:
            d['num_vehiculos_solicitados'] = d.get('num_vehiculos_solicitados') or 0
            d['num_vehiculos_fuera_programacion'] = d.get('num_vehiculos_fuera_programacion') or 0
            total = d['num_vehiculos_fuera_programacion']
            solicitados = d['num_vehiculos_solicitados']
            d['porcentaje'] = round((solicitados / total) * 100) if total > 0 else 0
    elif submenu == 'operaciones6':
        for d in data:
            d['num_vehiculos_fallas'] = d.get('num_vehiculos_fallas') or 0
            d['total_vehiculos_despachados'] = d.get('total_vehiculos_despachados') or 0
            total = d['total_vehiculos_despachados']
            fallas = d['num_vehiculos_fallas']
            d['porcentaje'] = round((fallas / total) * 100) if total > 0 else 0
    elif submenu == 'operaciones7':
        for d in data:
            d['num_conductores_arqueo_mes'] = d.get('num_conductores_arqueo_mes') or 0
            d['total_conductores_mes'] = d.get('total_conductores_mes') or 0
            total = d['total_conductores_mes']
            arqueo = d['num_conductores_arqueo_mes']
            d['porcentaje'] = round((arqueo / total) * 100) if total > 0 else 0
    elif submenu == 'operaciones8':
        for d in data:
            d['num_servicios_flota_propia'] = d.get('num_servicios_flota_propia') or 0
            d['total_servicios_prestados_mes'] = d.get('total_servicios_prestados_mes') or 0
            total = d['total_servicios_prestados_mes']
            propios = d['num_servicios_flota_propia']
            d['porcentaje'] = round((propios / total) * 100) if total > 0 else 0
    elif submenu == 'financieros1':
        for d in data:
            d['presupuesto_ejecutado'] = d.get('presupuesto_ejecutado') or 0
            d['presupuesto_proyectado'] = d.get('presupuesto_proyectado') or 0
            total = d['presupuesto_proyectado']
            ejecutado = d['presupuesto_ejecutado']
            d['porcentaje'] = round((ejecutado / total) * 100) if total > 0 else 0
    elif submenu == 'financieros2':
        for d in data:
            d['num_confiables'] = d.get('num_confiables') or 0
            d['num_total'] = d.get('num_total') or 0
            total = d['num_total']
            confiables = d['num_confiables']
            d['porcentaje'] = round((confiables / total) * 100) if total > 0 else 0
    elif submenu == 'comercial2':
        pass # No hay lógica de porcentaje para esta meta, solo la meta
    elif submenu == 'comercial3':
        pass # No hay lógica de porcentaje para esta meta, solo la meta
    elif submenu == 'comercial4':
        pass # No hay lógica de porcentaje para esta meta, solo la meta
    elif submenu == 'comercial5':
        pass # No hay lógica de porcentaje para esta meta, solo la meta
    elif submenu == 'comercial6':
        pass # No hay lógica de porcentaje para esta meta, solo la meta
    elif submenu == 'comercial7':
        pass # No hay lógica de porcentaje para esta meta, solo la meta
    elif submenu == 'comercial8':
        pass # No hay lógica de porcentaje para esta meta, solo la meta
    elif submenu == 'sst1':
        pass # No hay lógica de porcentaje para esta meta, solo la meta
    elif submenu == 'sst2':
        for d in data:
            # Asegúrate de que los campos existan y tengan valor numérico o '-'
            d['costos_siniestros_viales'] = d.get('costos_siniestros_viales', '-') or '-'
            d['costos_directos_siniestros_viales'] = d.get('costos_directos_siniestros_viales', '-') or '-'
            d['costos_indirectos_siniestros_viales'] = d.get('costos_indirectos_siniestros_viales', '-') or '-'
    elif submenu == 'sst3':
        pass # No hay lógica de porcentaje para esta meta, solo la meta
    elif submenu == 'sst4':
        pass # No hay lógica de porcentaje para esta meta, solo la meta
    elif submenu == 'sst5':
        pass # No hay lógica de porcentaje para esta meta, solo la meta
    elif submenu == 'sst6':
        pass # No hay lógica de porcentaje para esta meta, solo la meta
    elif submenu == 'sst9':
        pass # No hay lógica de porcentaje para esta meta, solo la meta
    elif submenu == 'sst10':
        pass # No hay lógica de porcentaje para esta meta, solo la meta
    elif submenu == 'sst11':
        pass # No hay lógica de porcentaje para esta meta, solo la meta
    elif submenu == 'sst12':
        pass # No hay lógica de porcentaje para esta meta, solo la meta
    elif submenu == 'sst13':
        pass # No hay lógica de porcentaje para esta meta, solo la meta
    elif submenu == 'sst14':
        pass # No hay lógica de porcentaje para esta meta, solo la meta
    elif submenu == 'sst15':
        pass # No hay lógica de porcentaje para esta meta, solo la meta
    elif submenu == 'sst16':
        pass # No hay lógica de porcentaje para esta meta, solo la meta
    elif submenu == 'sst17':
        pass # No hay lógica de porcentaje para esta meta, solo la meta
    elif submenu == 'sst18':
        pass # No hay lógica de porcentaje para esta meta, solo la meta
    elif submenu == 'sst19':
        pass # No hay lógica de porcentaje para esta meta, solo la meta
    elif submenu == 'sst20':
        pass # No hay lógica de porcentaje para esta meta, solo la meta
    elif submenu == 'talento1':
        pass # No hay lógica de porcentaje para esta meta, solo la meta
    elif submenu == 'talento2':
        pass # No hay lógica de porcentaje para esta meta, solo la meta
    elif submenu == 'talento3':
        pass # No hay lógica de porcentaje para esta meta, solo la meta
    elif submenu == 'talento4':
        pass # No hay lógica de porcentaje para esta meta, solo la meta
    elif submenu == 'talento5':
        pass # No hay lógica de porcentaje para esta meta, solo la meta
    elif submenu == 'talento6':
        pass # No hay lógica de porcentaje para esta meta, solo la meta
    elif submenu == 'talento7':
        pass # No hay lógica de porcentaje para esta meta, solo la meta
    elif submenu == 'talento8':
        pass # No hay lógica de porcentaje para esta meta, solo la meta
    elif submenu == 'talento9':
        pass # No hay lógica de porcentaje para esta meta, solo la meta
    elif submenu == 'talento10':
        pass # No hay lógica de porcentaje para esta meta, solo la meta
    elif submenu == 'seguridad1':
        pass # No hay lógica de porcentaje para esta meta, solo la meta
    elif submenu == 'seguridad2':
        pass # No hay lógica de porcentaje para esta meta, solo la meta
    elif submenu == 'seguridad3':
        for d in data:
            d['num_vehiculos_exceso_velocidad'] = d.get('num_vehiculos_exceso_velocidad') or 0
            d['total_vehiculos_con_seguimiento'] = d.get('total_vehiculos_con_seguimiento') or 0
            total = d['total_vehiculos_con_seguimiento']
            excesos = d['num_vehiculos_exceso_velocidad']
            d['porcentaje'] = round((excesos / total) * 100) if total > 0 else 0
    elif submenu == 'operaciones9':
        for d in data:
            d['num_mantenimientos_preventivos'] = d.get('num_mantenimientos_preventivos') or 0
            d['total_mantenimientos_programados'] = d.get('total_mantenimientos_programados') or 0
            total = d['total_mantenimientos_programados']
            preventivos = d['num_mantenimientos_preventivos']
            d['porcentaje'] = round((preventivos / total) * 100) if total > 0 else 0
    elif submenu == 'operaciones10':
        for d in data:
            d['total_novedades'] = d.get('total_novedades') or 0
            d['total_novedades_atendidas'] = d.get('total_novedades_atendidas') or 0
            total = d['total_novedades']
            atendidas = d['total_novedades_atendidas']
            d['porcentaje'] = round((atendidas / total) * 100) if total > 0 else 0

    # Normaliza los campos para evitar valores vacíos o nulos
    for d in data:
        for key, value in d.items():
            if value in [None, '', 'None']:
                d[key] = '-'
        if d.get('analisis_datos') in [None, '', 'None', '-']:
            d['analisis_datos'] = 'Sin información.'
        if d.get('analisis_causas') in [None, '', 'None', '-']:
            d['analisis_causas'] = 'Sin información.'
    # Devuelve los datos y la meta en formato JSON
    return Response({"data": data, "meta": meta})

# --- API REST para indicadores anuales de cualquier submenú ---
def indicadores_anual_api(request, submenu):
    # Obtiene el año actual
    año_actual = datetime.now().year
    # Filtra los indicadores del submenú y año actual
    indicadores = Indicador.objects.filter(
        submenu=submenu,
        periodo=año_actual
    ).order_by('mes')
    data = []
    for i in indicadores:
        data.append({
            'mes': i.mes,
            'porcentaje': i.porcentaje,
        })
    # Obtiene la meta dinámica desde la base de datos
    try:
        meta_obj = Meta.objects.get(submenu=submenu)
        meta_info = {
            'tipo': meta_obj.tipo,
            'valor': meta_obj.valor,
            'descripcion': meta_obj.descripcion,
        }
    except Meta.DoesNotExist:
        meta_info = {}
    # Devuelve los datos anuales y la meta en formato JSON
    return JsonResponse({'indicadores': data, 'meta': meta_info})

# Vista protegida para generar y descargar el PDF de reporte de indicadores
# Genera el PDF con tabla, gráfica y análisis según el submenú y tipo de reporte

@login_required
def reporte_pdf(request, parte, subparte, tipo):
    # Construye el nombre del submenú según los parámetros recibidos
    parte_lower = parte.lower()
    subparte_lower = subparte.lower()
    submenu = None
    if parte_lower == 'tic':
        if subparte == '1':
            submenu = 'tic1'
        elif subparte == '2':
            submenu = 'tic2'
        elif subparte == '3':
            submenu = 'tic3'
        elif subparte == '4':
            submenu = 'tic4'
    # Si el submenú no es válido, retorna error
    if not submenu:
        from django.http import HttpResponse
        return HttpResponse("Submenú no válido", status=400)
    # Filtra los indicadores y obtiene la meta
    indicadores = Indicador.objects.filter(submenu=submenu).order_by('periodo', 'mes')
    data = list(indicadores.values())
    try:
        meta_obj = Meta.objects.get(submenu=submenu)
        meta_val = meta_obj.valor
    except Meta.DoesNotExist:
        meta_val = None
    # Si el tipo es mensual, filtra solo el último mes disponible
    if tipo == 'mensual' and data:
        meses_orden = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
        data.sort(key=lambda d: (d.get('periodo', ''), meses_orden.index(d.get('mes', '')) if d.get('mes', '') in meses_orden else -1))
        ultimo_mes = data[-1]['mes']
        data = [d for d in data if d.get('mes', '') == ultimo_mes]
    # Define los campos de la tabla según el submenú
    if submenu == 'financieros1':
        campos = [
            ('periodo', 'Periodo'),
            ('mes', 'Mes'),
            ('porcentaje', '% Ejecución'),
            ('presupuesto_ejecutado', 'Presupuesto ejecutado'),
            ('presupuesto_proyectado', 'Presupuesto proyectado'),
        ]
    elif submenu == 'financieros2':
        campos = [
            ('periodo', 'Periodo'),
            ('mes', 'Mes'),
            ('porcentaje', 'Confiabilidad asociado negocio-proveedor (%)'),
            ('num_confiables', 'N° Proveedores analizados de calificación confiable'),
            ('num_total', 'N° Total de asociados de negocio analizados'),
        ]
    elif submenu == 'financieros3':
        campos = [
            ('periodo', 'Periodo'),
            ('mes', 'Mes'),
            ('porcentaje', '% Reevaluación'),
            ('calificacion_reevaluados', 'Calificación proveedores en reevaluación analizados durante el periodo'),
            ('num_total', 'Número Total de proveedores analizados en el periodo'),
        ]
    else:
        campos = [
            ('periodo', 'Periodo'),
            ('mes', 'Mes'),
            ('porcentaje', '% Fallas'),
            ('tickets_cerrados', 'Tickets cerrados'),
            ('tickets_abiertos_hardware', 'Tickets abiertos hardware'),
            ('tickets_abiertos_software', 'Tickets abiertos software'),
            ('total_copias_realizadas', 'Total copias realizadas'),
            ('total_copias_seguridad_exitosa', 'Total copias de seguridad exitosa'),
            ('ataques_ciberseguridad', 'Ataques ciberseguridad'),
            ('total_equipos', 'Total de equipos'),
            ('porcentaje_fallas_seguridad', '% Fallas seguridad'),
            ('porcentaje_cumplimiento_programa', '% Cumplimiento programa'),
            ('mantenimientos_programados', '# Mantenimientos programados'),
            ('total_mantenimientos_realizados', '# Total mantenimientos realizados'),
        ]
    # Detectar columnas con al menos un dato no vacío o no None
    columnas_usar = []
    for key, label in campos:
        if any(d.get(key) not in [None, '', 'None'] for d in data):
            columnas_usar.append((key, label))
    if not columnas_usar:
        columnas_usar = [('mes', 'Mes'), ('porcentaje', '% Fallas')]  # fallback mínimo
    table_data = [[label for _, label in columnas_usar]]
    for d in data:
        row = []
        for key, _ in columnas_usar:
            val = d.get(key)
            if val is None or str(val) == 'None':
                val = '-'
            row.append(str(val))
        table_data.append(row)
    ncols = len(columnas_usar)
    col_width = max((letter[0]-80) / ncols, 60)
    font_size = 11 if ncols <= 7 else 8
    table = Table(table_data, repeatRows=1, colWidths=[col_width]*ncols)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#193F77')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,0), font_size),
        ('FONTSIZE', (0,1), (-1,-1), font_size-1),
        ('BOTTOMPADDING', (0,0), (-1,0), 8),
        ('BACKGROUND', (0,1), (-1,-1), colors.white),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#6D6F72')),
    ]))
    for i, d in enumerate(data, start=1):
        for j, (key, _) in enumerate(campos):
            if key == 'porcentaje' and meta_val is not None and d.get('porcentaje', 0) < meta_val:
                table.setStyle([('TEXTCOLOR', (j,i), (j,i), colors.red)])
    from reportlab.platypus import Frame, Spacer
    from reportlab.lib.units import mm
    frame_height = 140 if ncols <= 7 else 180
    pdf_buffer = io.BytesIO()
    c = canvas.Canvas(pdf_buffer, pagesize=letter)
    width, height = letter
    # Encabezado personalizado con logo y datos del reporte
    logo_path = settings.BASE_DIR / 'sig' / 'static' / 'img' / 'logo.jpg'
    try:
        c.drawImage(ImageReader(str(logo_path)), 40, height-80, width=90, height=50, preserveAspectRatio=True, mask='auto')
    except Exception:
        pass
    c.setStrokeColorRGB(0.2, 0.3, 0.4)
    c.setLineWidth(1.2)
    c.line(40, height-90, width-40, height-90)
    c.setFont('Helvetica-Bold', 13)
    c.drawCentredString(width/2, height-60, 'FICHA REPORTE INDICADORES GESTIÓN')
    c.setFont('Helvetica-Bold', 11)
    c.drawString(180, height-80, 'SIG-FO-008')
    c.setFont('Helvetica', 11)
    c.drawString(300, height-80, 'VERSIÓN 06')
    c.drawString(400, height-80, datetime.now().strftime('%d/%m/%Y'))
    c.drawString(500, height-80, 'Pág. 1 de 1')
    c.setStrokeColorRGB(0.2, 0.3, 0.4)
    c.setLineWidth(2)
    c.line(40, height-95, width-40, height-95)
    c.setFont('Helvetica-Bold', 15)
    c.drawString(60, height-120, f'Reporte {parte.upper()} {subparte}')
    c.setFont('Helvetica', 10)
    c.drawString(60, height-135, f'Fecha de generación: {datetime.now().strftime("%d/%m/%Y %H:%M")}')
    frame = Frame(40, height-320, width-80, frame_height, showBoundary=0)
    story = [table, Spacer(1, 10*mm)]
    frame.addFromList(story, c)
    # Gráfica debajo de la tabla
    if data:
        x_labels = [d.get('mes', d.get('periodo', '')) for d in data]
        y_values = [d.get('porcentaje', 0) for d in data]
        fig, ax = plt.subplots(figsize=(6,3))
        bar_colors = ['#64ABDE', '#6D6F72', '#193F77', '#3C3D3F']
        ax.bar(x_labels, y_values, color=[bar_colors[i%len(bar_colors)] for i in range(len(x_labels))])
        ax.set_xlabel('Mes' if 'mes' in data[0] else 'Periodo')
        ax.set_ylabel('%')
        ax.set_title('Indicadores')
        ax.set_ylim(0, 100)
        buf = io.BytesIO()
        plt.tight_layout()
        plt.savefig(buf, format='png')
        plt.close(fig)
        buf.seek(0)
        c.drawImage(ImageReader(buf), 40, height-480, width=500, height=150)
    # --- TABLA DE ANÁLISIS ---
    analisis_data = []
    vistos = set()
    for d in data:
        key = (d.get('mes', ''), d.get('analisis_datos', ''), d.get('analisis_causas', ''))
        if key not in vistos:
            analisis_data.append([
                d.get('mes', ''),
                d.get('analisis_datos', ''),
                d.get('analisis_causas', '')
            ])
            vistos.add(key)
    if analisis_data:
        analisis_table = Table([
            ['MES', 'ANÁLISIS DE DATOS', 'ANÁLISIS DE CAUSAS']
        ] + analisis_data, repeatRows=1, colWidths=[80, 220, 180])
        analisis_table.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#e6f0fa')),
            ('TEXTCOLOR', (0,0), (-1,0), colors.HexColor('#003366')),
            ('ALIGN', (0,0), (-1,-1), 'CENTER'),
            ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
            ('FONTSIZE', (0,0), (-1,0), 10),
            ('FONTSIZE', (0,1), (-1,-1), 9),
            ('BOTTOMPADDING', (0,0), (-1,0), 6),
            ('BACKGROUND', (0,1), (-1,-1), colors.white),
            ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#b0c4de')),
        ]))
        frame_analisis = Frame(40, height-650, width-80, 120, showBoundary=0)
        from reportlab.platypus import Flowable
        story_analisis = [analisis_table]  # type: list[Flowable]
        frame_analisis.addFromList(story_analisis, c)
    c.showPage()
    c.save()
    pdf_buffer.seek(0)
    filename = f"reporte_{parte}_{subparte}_{tipo}.pdf"
    return FileResponse(pdf_buffer, as_attachment=True, filename=filename)

# Decorador para restringir acceso solo a los correos permitidos
allowed_emails_check = lambda u: u.is_authenticated and u.email in ALLOWED_EMAILS

# Vista protegida para editar indicadores desde el admin
# Permite actualizar los campos de un indicador existente

@user_passes_test(allowed_emails_check)
def editar_indicadores(request):
    from .models import Indicador
    indicadores = Indicador.objects.all().order_by('submenu', 'periodo', 'mes')
    mensaje = ''
    if request.method == 'POST':
        id_ = request.POST.get('id')
        indicador = Indicador.objects.get(id=id_)
        indicador.periodo = request.POST.get('periodo')
        indicador.mes = request.POST.get('mes')
        indicador.porcentaje = request.POST.get('porcentaje')
        indicador.analisis_datos = request.POST.get('analisis_datos')
        indicador.analisis_causas = request.POST.get('analisis_causas')
        indicador.save()
        mensaje = 'Registro actualizado correctamente.'
    return render(request, 'sig/editar_indicadores.html', {'indicadores': indicadores, 'mensaje': mensaje})