# Script para poblar la base de datos con datos de ejemplo para operaciones10 y sus subtabs
import os
import sys
import django
from datetime import datetime

# Agregar la raíz del proyecto al sys.path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'design.settings')
django.setup()

from design.sig.models import Indicador
from design.sig.models import Meta

# Datos de ejemplo para operaciones10 (General)
for mes, total, atendidas, porcentaje in [
    ('Enero', 20, 18, 90),
    ('Febrero', 22, 20, 91),
    ('Marzo', 18, 15, 83),
    ('Abril', 25, 22, 88),
    ('Mayo', 19, 17, 89),
    ('Junio', 21, 19, 90),
]:
    Indicador.objects.update_or_create(
        submenu='operaciones10', periodo='2025', mes=mes,
        defaults={
            'total_novedades': total,
            'total_novedades_atendidas': atendidas,
            'porcentaje': porcentaje
        }
    )

# Altas
for mes, reportadas, atendidas, porcentaje in [
    ('Enero', 8, 7, 88),
    ('Febrero', 9, 8, 89),
    ('Marzo', 7, 6, 86),
    ('Abril', 10, 9, 90),
    ('Mayo', 6, 5, 83),
    ('Junio', 8, 7, 88),
]:
    Indicador.objects.update_or_create(
        submenu='operaciones10_altas', periodo='2025', mes=mes,
        defaults={
            'num_novedades_reportadas_alta': reportadas,
            'num_novedades_atendidas': atendidas,
            'porcentaje': porcentaje
        }
    )

# Medias
for mes, reportadas, atendidas, porcentaje in [
    ('Enero', 6, 5, 83),
    ('Febrero', 7, 6, 86),
    ('Marzo', 5, 4, 80),
    ('Abril', 8, 7, 88),
    ('Mayo', 7, 6, 86),
    ('Junio', 6, 5, 83),
]:
    Indicador.objects.update_or_create(
        submenu='operaciones10_medias', periodo='2025', mes=mes,
        defaults={
            'num_novedades_reportadas_media': reportadas,
            'num_novedades_atendidas_media': atendidas,
            'porcentaje': porcentaje
        }
    )

# Bajas
for mes, reportadas, atendidas, porcentaje in [
    ('Enero', 6, 6, 100),
    ('Febrero', 6, 6, 100),
    ('Marzo', 6, 5, 83),
    ('Abril', 7, 6, 86),
    ('Mayo', 6, 5, 83),
    ('Junio', 7, 6, 86),
]:
    Indicador.objects.update_or_create(
        submenu='operaciones10_bajas', periodo='2025', mes=mes,
        defaults={
            'num_novedades_reportadas_baja': reportadas,
            'num_novedades_atendidas_baja': atendidas,
            'porcentaje': porcentaje
        }
    )

# Reportes supervisor
for mes, reportes, atendidos in [
    ('Enero', 3, 3),
    ('Febrero', 4, 4),
    ('Marzo', 2, 2),
    ('Abril', 3, 3),
    ('Mayo', 2, 2),
    ('Junio', 3, 3),
]:
    Indicador.objects.update_or_create(
        submenu='operaciones10_reportes', periodo='2025', mes=mes,
        defaults={
            'num_reportes_supervisor': reportes,
            'num_atendidos_supervisor': atendidos,
            'porcentaje': 100
        }
    )

# Meta para operaciones10 (si no existe)
Meta.objects.update_or_create(
    submenu='operaciones10',
    defaults={'valor': 80, 'tipo': 'mayor'}
)

# Metas para operaciones3 a operaciones9
metas_ops = [
    ('operaciones3', 4, 'menor'),
    ('operaciones4', 98, 'mayor'),
    ('operaciones5', 95, 'mayor'),
    ('operaciones6', 20, 'menor'),
    ('operaciones7', 0, 'igual'),
    ('operaciones8', 90, 'mayor'),
    ('operaciones9', 85, 'mayor'),
]
for submenu, valor, tipo in metas_ops:
    Meta.objects.update_or_create(
        submenu=submenu,
        defaults={'valor': valor, 'tipo': tipo}
    )

# Datos de ejemplo para TICs 3 (Incidentes de seguridad informática)
datos_tic3 = [
    {'submenu': 'tic3', 'periodo': '2024', 'mes': 'Enero', 'ataques_ciberseguridad': 2, 'total_equipos': 100, 'porcentaje': 2},
    {'submenu': 'tic3', 'periodo': '2024', 'mes': 'Febrero', 'ataques_ciberseguridad': 1, 'total_equipos': 100, 'porcentaje': 1},
    {'submenu': 'tic3', 'periodo': '2024', 'mes': 'Marzo', 'ataques_ciberseguridad': 3, 'total_equipos': 100, 'porcentaje': 3},
    {'submenu': 'tic3', 'periodo': '2024', 'mes': 'Abril', 'ataques_ciberseguridad': 0, 'total_equipos': 100, 'porcentaje': 0},
    {'submenu': 'tic3', 'periodo': '2024', 'mes': 'Mayo', 'ataques_ciberseguridad': 4, 'total_equipos': 100, 'porcentaje': 4},
    {'submenu': 'tic3', 'periodo': '2024', 'mes': 'Junio', 'ataques_ciberseguridad': 2, 'total_equipos': 100, 'porcentaje': 2},
]

# Datos de ejemplo para TICs 4 (Cumplimiento en el programa de mantenimiento de TICs)
datos_tic4 = [
    {'submenu': 'tic4', 'periodo': '2024', 'mes': 'Enero', 'mantenimientos_programados': 10, 'total_mantenimientos_realizados': 9, 'porcentaje': 90},
    {'submenu': 'tic4', 'periodo': '2024', 'mes': 'Febrero', 'mantenimientos_programados': 10, 'total_mantenimientos_realizados': 10, 'porcentaje': 100},
    {'submenu': 'tic4', 'periodo': '2024', 'mes': 'Marzo', 'mantenimientos_programados': 10, 'total_mantenimientos_realizados': 8, 'porcentaje': 80},
    {'submenu': 'tic4', 'periodo': '2024', 'mes': 'Abril', 'mantenimientos_programados': 10, 'total_mantenimientos_realizados': 10, 'porcentaje': 100},
    {'submenu': 'tic4', 'periodo': '2024', 'mes': 'Mayo', 'mantenimientos_programados': 10, 'total_mantenimientos_realizados': 7, 'porcentaje': 70},
    {'submenu': 'tic4', 'periodo': '2024', 'mes': 'Junio', 'mantenimientos_programados': 10, 'total_mantenimientos_realizados': 10, 'porcentaje': 100},
]

# Insertar datos TIC3
def insertar_tic3():
    for d in datos_tic3:
        obj, created = Indicador.objects.update_or_create(
            submenu=d['submenu'], periodo=d['periodo'], mes=d['mes'],
            defaults={
                'ataques_ciberseguridad': d['ataques_ciberseguridad'],
                'total_equipos': d['total_equipos'],
                'porcentaje': d['porcentaje'],
            }
        )
        print(f"{'Creado' if created else 'Actualizado'}: {obj}")

# Insertar datos TIC4
def insertar_tic4():
    for d in datos_tic4:
        obj, created = Indicador.objects.update_or_create(
            submenu=d['submenu'], periodo=d['periodo'], mes=d['mes'],
            defaults={
                'mantenimientos_programados': d['mantenimientos_programados'],
                'total_mantenimientos_realizados': d['total_mantenimientos_realizados'],
                'porcentaje': d['porcentaje'],
            }
        )
        print(f"{'Creado' if created else 'Actualizado'}: {obj}")

if __name__ == '__main__':
    insertar_tic3()
    insertar_tic4()
    print('Datos de ejemplo insertados para TIC3 y TIC4.') 