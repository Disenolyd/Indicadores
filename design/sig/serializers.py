from rest_framework import serializers
from .models import Indicador

# Serializer para exponer los datos del modelo Indicador vía API REST
class IndicadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Indicador
        # Lista de campos que se exponen en la API
        fields = [
            'submenu',
            'periodo',
            'mes',
            'porcentaje',
            'analisis_datos',
            'analisis_causas',
            'tickets_cerrados',
            'tickets_abiertos_hardware',
            'tickets_abiertos_software',
            'total_copias_realizadas',
            'total_copias_seguridad_exitosa',
            'ataques_ciberseguridad',
            'total_equipos',
            'porcentaje_cumplimiento_programa',
            'mantenimientos_programados',
            'total_mantenimientos_realizados',
            'presupuesto_ejecutado',
            'presupuesto_proyectado',
            # --- Operaciones campos generales y operaciones10 ---
            'num_no_utilizadas',
            'total_disponibles',
            'num_sin_novedad',
            'total_despachos',
            'sum_no_retorno',
            'total_servicios',
            'num_entregados_tiempo',
            'total_servicios_prestados',
            'num_vehiculos_solicitados',
            'num_vehiculos_fuera_programacion',
            'num_vehiculos_fallas',
            'num_vehiculos_solicitados_mes',
            'num_conductores_arqueo_mes',
            'num_conductores_novedad_arqueo',
            'num_servicios_flota_propia',
            'num_total_servicios',
            'num_mantenimientos_preventivos',
            'num_mantenimientos_predictivos',
            'num_mantenimientos_correctivos',
            'num_mantenimientos_pendientes',
            'num_mantenimientos_cumplidos',
            'total_novedades',
            'total_novedades_atendidas',
            # --- Operaciones10 subtabs ---
            'num_novedades_reportadas_alta',
            'num_novedades_atendidas',
            'num_novedades_reportadas_media',
            'num_novedades_atendidas_media',
            'num_novedades_reportadas_baja',
            'num_novedades_atendidas_baja',
            # --- Para reportes supervisor ---
            'num_reportadas_alta',
            'num_atendidas_alta',
            'num_reportadas_media',
            'num_atendidas_media',
            'num_reportadas_baja',
            'num_atendidas_baja',
            'num_reportes_supervisor',
            'num_atendidos_supervisor',
            'num_confiables',
            'calificacion_reevaluados',
            'num_total',
            # --- Comercial1: Satisfacción del cliente ---
            'grado_satisfaccion_cliente',
            'num_clientes_superior_a',
            'num_clientes_evaluados',
            # --- Comercial2: Confiabilidad de asociado cliente ---
            'confiabilidad_asociado_cliente',
            'num_asociados_confiables',
            'num_total_clientes',
            # --- Comercial3: Nuevos negocios ---
            'porcentaje_nuevos_negocios',
            'ingresos_nuevos_negocios',
            'meta_nuevos_negocios',
            # --- Comercial4: Grado de cumplimiento de la Facturación ---
            'porcentaje_grado_cumplimiento',
            'facturas_radicadas_tiempo',
            'total_facturas_radicadas',
            # --- Comercial5: Tiempo promedio de cierre PQRS ---
            'tiempo_promedio_cierre_pqrs',
            'promedio_tiempos_cierre_pqrsrf',
            'tiempo_respuesta',
            # --- Comercial6: % Total de PQRS ---
            'porcentaje_total_pqrs',
            'num_pqrsf_recibidas',
            'total_servicios_periodo',
            # --- Comercial7: % Salidas no conformes respecto al total de servicios prestados ---
            'porcentaje_salidas_no_conformes',
            'num_salidas_no_conformes',
            'total_servicios',
            # --- Comercial8: Efectividad ofertas comerciales ---
            'efectividad_ofertas_comerciales',
            'num_cotizaciones_aprobadas',
            'total_cotizaciones_enviados',
            # --- Talento1: Confiabilidad asociado de negocio-empleado ---
            'confiabilidad_asociado_negocio',
            'calificacion_promedio',
            'calificacion_maxima',
            # --- Talento2: Eficacia programa de capacitación ---
            'eficacia_programa_capacitacion',
            'promedio_capacitaciones_eficaces',
            # --- Talento3: Cobertura de capacitación ---
            'cobertura_capacitacion',
            'trabajadores_asistieron',
            'trabajadores_convocados',
            # --- Talento4: Rotación de personal ---
            'rotacion_personal',
            'personal_contratado',
            'personal_desvinculado',
            'trabajadores_inicio_mes',
            'trabajadores_fin_mes',
            # --- Talento5: Evaluación desempeño ---
            'evaluacion_desempeno',
            'ponderacion_evaluaciones_aplicadas',
            # --- Talento6: Tasa de ausentismo laboral ---
            'tasa_ausentismo_laboral',
            'total_h_ausentismo',
            'total_h_planificadas',
            # --- Talento7: Horas extras ---
            'porcentaje_het',
            'horas_extras_trabajadas',
            'horas_deben_trabajarse',
            # --- Talento8: Tiempo de selección y contratación ---
            'porcentaje_tiempo_seleccion',
            'tiempo_proceso_seleccion',
            'num_contrataciones',
            # --- Talento9: Costo de contratación ---
            'costo_contratacion',
            'coste_reclutamiento_interno',
            'coste_reclutamiento_externo',
            'num_contrataciones_periodo',
            # --- Talento10: Tasa de recuperación de incapacidades ---
            'tasa_recuperacion_incapacidades',
            'incapacidades_radicadas_periodo',
            'incapacidades_para_cobro_periodo',
            # --- Seguridad1: Novedades viales vehículos ---
            'porcentaje_novedades_viales',
            'vehiculos_con_novedad',
            'vehiculos_programados',
            # --- Seguridad2: Inspecciones a instalaciones ---
            'porcentaje_cumplimiento_instalaciones',
            'sumatoria_incumplimiento',
            'calificacion_cumple_totalmente',
            # --- Seguridad3: Excesos de velocidad ---
            'num_vehiculos_exceso_velocidad',
            'total_vehiculos_mes',
            # --- Seguridad4: Novedades flota propia botones de pánico ---
            'sin_novedad',
            'total_botones_panico_prueba',
            'conductores_accionan_boton_panico_evento_critico',
            # --- SST1: Consolidado ---
            'num_siniestros_viales',
            'dato_numerador_sv',
            'dato_denominador_km',
            # --- SST2: Consolidado ---
            'costos_siniestros_viales',
            'costos_directos_siniestros_viales',
            'costos_indirectos_siniestros_viales',
            # --- SST3: Riesgos de Seguridad Vial Identificados ---
            'riesgos_seguridad_vial',
            'cantidad_riesgos_final_anio',
            'cantidad_riesgos_inicio_anio',
            # --- SST4: Gestión de riesgos viales ---
            'gestion_riesgos_viales',
            'cant_riesgos_valoracion_alta_final_anio',
            'cant_riesgos_valoracion_alta_inicio_anio',
            # --- SST5: Cumplimiento Metas PESV ---
            'cumplimiento',
            'num_metas_alcanzadas',
            'num_total_metas_definidas',
            # --- SST6: Cumplimiento de actividades plan anual ---
            'cumplimiento_actividades',
            'num_actividades_ejecutadas',
            'num_total_actividades_programadas',
            'num_actividades_ejecutadas_sst22',  # SST22: # de actividades ejecutadas
            'num_actividades_programadas_sst22',  # SST22: # total de actividades programadas
            # --- SST7: Exceso jornadas laborales ---
            'num_excesos_jornada',
            'total_dias_trabajados',
            # --- SST8: Cobertura programa de gestión velocidad empresarial ---
            'num_vehiculos_incluidos',
            'num_vehiculos_utilizados',
            # --- SST9: Excesos Límite de Velocidad Laboral ELVL ---
            'num_excesos_velocidad_laboral',
            'total_desplazamientos_laborales_mes',
            # --- SST10: Inspecciones Diarias Preoperacionales (IDP) ---
            'num_vehiculos_inspeccionados_diariamente',
            'total_vehiculos_trabajan_diariamente',
            # --- SST11: Cumplimiento plan mantenimiento preventivo de vehículos (CPMVh) ---
            'num_actividades_mantenimiento_ejecutadas',
            'total_actividades_mantenimiento_programadas',
            # --- SST12: Cobertura plan de formación en seguridad vial (CPF PESV) ---
            'num_capacitaciones_ejecutadas',
            'total_capacitaciones_programadas',
            'num_capacitaciones_ejecutadas_sst21',  # SST21: # de capacitaciones ejecutadas
            'num_capacitaciones_programadas_sst21',  # SST21: # total de capacitaciones programadas
            # --- SST13: No Conformidades Auditoria Cerradas_NCAC ---
            'num_no_conformidades_identificadas_analizadas',
            'num_no_conformidades_gestionadas_cerradas',
            # --- SST14: Frecuencia de Accidentalidad ---
            'total_at_mes',
            'num_trabajadores_mes',
            # --- SST15: Severidad de accidentalidad ---
            'dias_incapacidad_at_mes',
            'dias_cargados_mes',
            'num_trabajadores_mes',
            # --- SST16: Proporción de accidentes de trabajo mortales en el año ---
            'num_at_mortales_anio',  # sst16
            'total_at_anio', 
            #   --- SST17: Cumplimiento en la ejecucion de alcoholimetrías ---
            'num_pruebas_positivas',
            'num_empleados',
            'num_pruebas_realizadas',
            # --- SST18: Inspecciones de seguridad ---
            'cantidad_novedades_locativas',      # sst18
            'total_inspecciones_elaboradas',     # sst18
            'num_novedades_cerradas',  # SST19: # de novedades cerradas
            'num_novedades_reportadas',  # SST19: # total de novedades reportadas
            'num_requisitos_establecidos',  # SST20: # de requisitos establecidos
            'num_total_requisitos',  # SST20: # total de requisitos
            'num_incidentes_reportados_sst23',  # SST23: # Incidentes reportados oportunamente SST
            'num_total_incidentes_sst23',  # SST23: # Total de incidentes ocurridos en el periodo
            'num_casos_el_sst24',  # SST24: # Casos nuevos y antiguos de EL en el año
            'promedio_trabajadores_sst24',  # SST24: Promedio trabajadores en el año
            'num_casos_nuevos_el_sst25',  # SST25: # Casos nuevos Enfermedad Laboral en el año
            'promedio_trabajadores_sst25',  # SST25: Promedio de trabajadores en el año
            'num_dias_ausencia_sst26',  # SST26: # de días de ausencia por incapacidad laboral o común
            'num_dias_trabajo_programados_sst26',  # SST26: # de días de trabajo programados
            'num_trabajadores_sst26',  # SST26: # de trabajadores
            'dias_laborados_mes_sst26',  # SST26: días laborados mes
        ]
