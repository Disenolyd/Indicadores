from django.contrib import admin
from django.urls import path
from sig.views import home, custom_login, custom_logout, indicadores_api, reporte_pdf, editar_indicadores, indicadores_anual_api
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.http import FileResponse

urlpatterns = [
    path('admin/', admin.site.urls),  # Panel de administración de Django (gestión de usuarios, modelos, metas, etc.)
    path('home/', home, name='home'),  # Vista principal del sistema (dashboard con indicadores y reportes)
    path('login/', custom_login, name='login'),  # Vista de inicio de sesión personalizada (solo usuarios autorizados)
    path('logout/', custom_logout, name='logout'),  # Cerrar sesión y redirigir a login
    path('api/indicadores/<str:submenu>/', indicadores_api, name='indicadores_api'),  # API REST para obtener indicadores y meta de un submenú (mensual, trimestral, semestral)
    path('api/indicadores-anual/<str:submenu>/', indicadores_anual_api, name='indicadores_anual_api'),  # API REST para obtener indicadores y meta anual de cualquier submenú
    path('reporte_pdf/<str:parte>/<str:subparte>/<str:tipo>/', reporte_pdf, name='reporte_pdf'),  # Generar y descargar PDF de reporte con tabla, gráfica y análisis
    path('editar-indicadores/', editar_indicadores, name='editar_indicadores'),  # Vista protegida para editar indicadores desde el admin
    path('', home, name='home_root'),  # Redirección raíz a la vista principal (dashboard)
]