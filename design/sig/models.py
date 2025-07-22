from django.db import models
from django.core.exceptions import ValidationError

# --- Modelo principal de indicadores ---
class Indicador(models.Model):
    # Identificador del submenú (ej: 'tic1', 'financieros1', etc.)
    submenu = models.CharField(max_length=50)
    # Año o periodo (ej: '2024')
    periodo = models.CharField(max_length=10)
    # Mes (ej: 'Enero', puede ser null)
    mes = models.CharField(max_length=20, blank=True, null=True)
    # Valor del indicador (porcentaje principal)
    porcentaje = models.FloatField()
    # Análisis de datos y causas para la tabla de análisis
    analisis_datos = models.TextField(blank=True, null=True)
    analisis_causas = models.TextField(blank=True, null=True)
    # Campos para operaciones
    num_no_utilizadas = models.IntegerField(null=True, blank=True)  # Operaciones: posiciones no utilizadas
    total_disponibles = models.IntegerField(null=True, blank=True)  # Operaciones: total posiciones disponibles
    num_sin_novedad = models.IntegerField(null=True, blank=True)  # Operaciones: despachos sin novedad
    total_despachos = models.IntegerField(null=True, blank=True)  # Operaciones: total despachos
    sum_no_retorno = models.IntegerField(null=True, blank=True)  # Operaciones: suma no retorno
    total_servicios = models.IntegerField(null=True, blank=True)  # Operaciones: total servicios
    num_entregados_tiempo = models.IntegerField(null=True, blank=True)  # Operaciones: entregados a tiempo
    total_servicios_prestados = models.IntegerField(null=True, blank=True)  # Operaciones: servicios prestados
    # NUEVOS CAMPOS para los submenús que faltan:
    num_vehiculos_solicitados = models.IntegerField(null=True, blank=True)  # Vehículos solicitados
    num_vehiculos_fuera_programacion = models.IntegerField(null=True, blank=True)  # Vehículos fuera de programación
    num_vehiculos_fallas = models.IntegerField(null=True, blank=True)  # Vehículos con fallas
    num_vehiculos_solicitados_mes = models.IntegerField(null=True, blank=True)  # Vehículos solicitados en el mes
    num_conductores_arqueo_mes = models.IntegerField(null=True, blank=True)  # Conductores con arqueo en el mes
    num_conductores_novedad_arqueo = models.IntegerField(null=True, blank=True)  # Conductores con novedad en arqueo
    num_servicios_flota_propia = models.IntegerField(null=True, blank=True)  # Servicios flota propia
    num_total_servicios = models.IntegerField(null=True, blank=True)  # Total servicios
    num_mantenimientos_preventivos = models.IntegerField(null=True, blank=True)  # Mantenimientos preventivos
    num_mantenimientos_predictivos = models.IntegerField(null=True, blank=True)  # Mantenimientos predictivos
    num_mantenimientos_correctivos = models.IntegerField(null=True, blank=True)  # Mantenimientos correctivos
    num_mantenimientos_pendientes = models.IntegerField(null=True, blank=True)  # Mantenimientos pendientes
    num_mantenimientos_cumplidos = models.IntegerField(null=True, blank=True)  # Mantenimientos cumplidos
    total_novedades = models.IntegerField(null=True, blank=True)  # Total novedades
    total_novedades_atendidas = models.IntegerField(null=True, blank=True)  # Novedades atendidas
    # Campos para TIC (agrega después de los de operaciones)
    tickets_cerrados = models.IntegerField(null=True, blank=True)  # TIC: tickets cerrados
    tickets_abiertos_hardware = models.IntegerField(null=True, blank=True)  # TIC: tickets abiertos hardware
    tickets_abiertos_software = models.IntegerField(null=True, blank=True)  # TIC: tickets abiertos software
    total_copias_realizadas = models.IntegerField(null=True, blank=True)  # TIC: copias realizadas
    total_copias_seguridad_exitosa = models.IntegerField(null=True, blank=True)  # TIC: copias de seguridad exitosas
    ataques_ciberseguridad = models.IntegerField(null=True, blank=True)  # TIC: ataques ciberseguridad
    total_equipos = models.IntegerField(null=True, blank=True)  # TIC: total equipos
    porcentaje_cumplimiento_programa = models.FloatField(null=True, blank=True)  # TIC: % cumplimiento programa
    mantenimientos_programados = models.IntegerField(null=True, blank=True)  # TIC: mantenimientos programados
    total_mantenimientos_realizados = models.IntegerField(null=True, blank=True)  # TIC: mantenimientos realizados
    num_novedades_reportadas_alta = models.IntegerField(null=True, blank=True)  # Operaciones10: novedades alta
    num_novedades_atendidas = models.IntegerField(null=True, blank=True)  # Operaciones10: novedades atendidas alta
    num_novedades_reportadas_media = models.IntegerField(null=True, blank=True)  # Operaciones10: novedades media
    num_novedades_atendidas_media = models.IntegerField(null=True, blank=True)  # Operaciones10: novedades atendidas media
    num_novedades_reportadas_baja = models.IntegerField(null=True, blank=True)  # Operaciones10: novedades baja
    num_novedades_atendidas_baja = models.IntegerField(null=True, blank=True)  # Operaciones10: novedades atendidas baja
    num_reportes_supervisor = models.IntegerField(null=True, blank=True)  # Operaciones10: reportes supervisor
    num_atendidos_supervisor = models.IntegerField(null=True, blank=True)  # Operaciones10: reportes atendidos supervisor
    # --- Financieros1: Ejecución de prevención ---
    presupuesto_ejecutado = models.FloatField(null=True, blank=True)  # Presupuesto ejecutado (financieros1)
    presupuesto_proyectado = models.FloatField(null=True, blank=True)  # Presupuesto proyectado (financieros1)
    # --- Financieros2: Confiabilidad asociado negocio-proveedor ---
    num_confiables = models.IntegerField(null=True, blank=True)  # Número de proveedores analizados de calificación confiable (financieros2)
    num_total = models.IntegerField(null=True, blank=True)  # Número total de asociados de negocio analizados (financieros2 y financieros3)
    # --- Financieros3: Reevaluación de proveedores ---
    calificacion_reevaluados = models.IntegerField(null=True, blank=True)  # Calificación proveedores en reevaluación analizados durante el periodo (financieros3)
    # num_total ya está definido arriba y se reutiliza para financieros3
    # --- Comercial1: Satisfacción del cliente ---
    grado_satisfaccion_cliente = models.CharField(max_length=20, null=True, blank=True)  # Grado de satisfacción del cliente (puede ser '100%' o '#¡DIV/0!')
    num_clientes_superior_a = models.IntegerField(null=True, blank=True)  # # De clientes con calificación superior a
    num_clientes_evaluados = models.IntegerField(null=True, blank=True)  # Cantidad de clientes evaluados
    # --- Comercial2: Confiabilidad de asociado cliente ---
    confiabilidad_asociado_cliente = models.CharField(max_length=20, null=True, blank=True)  # Confiabilidad de asociado cliente (puede ser '100%' o '#¡DIV/0!')
    num_asociados_confiables = models.IntegerField(null=True, blank=True)  # # Asociados confiables
    num_total_clientes = models.IntegerField(null=True, blank=True)  # # Total de clientes
    # --- Comercial3: Nuevos negocios ---
    porcentaje_nuevos_negocios = models.CharField(max_length=20, null=True, blank=True)  # % Nuevos negocios (puede ser '100%' o '#¡DIV/0!')
    ingresos_nuevos_negocios = models.IntegerField(null=True, blank=True)  # Ingresos por nuevos negocios
    meta_nuevos_negocios = models.IntegerField(null=True, blank=True)  # Meta nuevos negocios
    # --- Comercial4: Grado de cumplimiento de la Facturación ---
    porcentaje_grado_cumplimiento = models.CharField(max_length=20, null=True, blank=True)  # % Grado cumplimiento (puede ser '94%' o '#¡DIV/0!')
    facturas_radicadas_tiempo = models.IntegerField(null=True, blank=True)  # # de facturas radicadas a tiempo
    total_facturas_radicadas = models.IntegerField(null=True, blank=True)  # # total de facturas radicadas
    # --- Comercial5: Tiempo promedio de cierre PQRS ---
    tiempo_promedio_cierre_pqrs = models.CharField(max_length=20, null=True, blank=True)  # Tiempo promedio de cierre PQRS (puede ser número o '#¡DIV/0!')
    promedio_tiempos_cierre_pqrsrf = models.FloatField(null=True, blank=True)  # Promedio de tiempos cierre PQSRF
    tiempo_respuesta = models.FloatField(null=True, blank=True)  # Tiempo de respuesta
    # --- Comercial6: % Total de PQRS ---
    porcentaje_total_pqrs = models.CharField(max_length=20, null=True, blank=True)  # % Total de PQRS (puede ser número o '#¡DIV/0!')
    num_pqrsf_recibidas = models.IntegerField(null=True, blank=True)  # # De PQRSF recibidas
    total_servicios_periodo = models.IntegerField(null=True, blank=True)  # Total servicios del periodo
    # --- Comercial7: % Salidas no conformes respecto al total de servicios prestados ---
    porcentaje_salidas_no_conformes = models.CharField(max_length=20, null=True, blank=True)  # % Salidas no conformes (puede ser número o '#¡DIV/0!')
    num_salidas_no_conformes = models.IntegerField(null=True, blank=True)  # Numero salidas no conformes
    total_servicios = models.IntegerField(null=True, blank=True)  # Total servicios
    # --- Comercial8: Efectividad ofertas comerciales ---
    efectividad_ofertas_comerciales = models.CharField(max_length=20, null=True, blank=True)  # Efectividad ofertas comerciales (puede ser número o '#¡DIV/0!')
    num_cotizaciones_aprobadas = models.IntegerField(null=True, blank=True)  # # De cotizaciones aprobadas
    total_cotizaciones_enviados = models.IntegerField(null=True, blank=True)  # Total cotizaciones enviados
    # --- Talento1: Confiabilidad asociado de negocio-empleado ---
    confiabilidad_asociado_negocio = models.CharField(max_length=20, null=True, blank=True)  # % Confiabilidad
    calificacion_promedio = models.CharField(max_length=20, null=True, blank=True)  # Calificación Promedio
    calificacion_maxima = models.CharField(max_length=20, null=True, blank=True)  # Calificación Máxima
    # --- Talento2: Eficacia programa de capacitación ---
    eficacia_programa_capacitacion = models.CharField(max_length=20, null=True, blank=True)  # % Eficacia
    promedio_capacitaciones_eficaces = models.CharField(max_length=20, null=True, blank=True)  # Promedio capacitaciones eficaces
    # --- Talento3: Cobertura de capacitación ---
    cobertura_capacitacion = models.CharField(max_length=20, null=True, blank=True)  # % Cobertura de capacitación
    trabajadores_asistieron = models.IntegerField(null=True, blank=True)  # Trabajadores que asistieron
    trabajadores_convocados = models.IntegerField(null=True, blank=True)  # Trabajadores convocados
    # --- Talento4: Rotación de personal ---
    rotacion_personal = models.CharField(max_length=20, null=True, blank=True)  # % Rotación de personal
    personal_contratado = models.IntegerField(null=True, blank=True)  # # Personal contratado
    personal_desvinculado = models.IntegerField(null=True, blank=True)  # # Personal desvinculado
    trabajadores_inicio_mes = models.IntegerField(null=True, blank=True)  # Trabajadores inicio mes
    trabajadores_fin_mes = models.IntegerField(null=True, blank=True)  # Trabajadores fin mes
    # --- Talento5: Evaluación desempeño ---
    evaluacion_desempeno = models.CharField(max_length=20, null=True, blank=True)  # % Evaluación desempeño
    ponderacion_evaluaciones_aplicadas = models.CharField(max_length=20, null=True, blank=True)  # Ponderación evaluaciones aplicadas
    # --- Talento6: Tasa de ausentismo laboral ---
    tasa_ausentismo_laboral = models.CharField(max_length=20, null=True, blank=True)  # % Tasa ausentismo laboral
    total_h_ausentismo = models.IntegerField(null=True, blank=True)  # Total # H. Ausentismo
    total_h_planificadas = models.IntegerField(null=True, blank=True)  # Total # H. Planificadas
    # --- Talento7: Horas extras ---
    porcentaje_het = models.CharField(max_length=20, null=True, blank=True)  # % H.E.T
    horas_extras_trabajadas = models.IntegerField(null=True, blank=True)  # # Horas extras trabajadas
    horas_deben_trabajarse = models.IntegerField(null=True, blank=True)  # # Horas que deben trabajarse
    # --- Talento8: Tiempo de selección y contratación ---
    porcentaje_tiempo_seleccion = models.CharField(max_length=20, null=True, blank=True)  # % Tiempo de selección
    tiempo_proceso_seleccion = models.IntegerField(null=True, blank=True)  # Tiempo proceso selección (días)
    num_contrataciones = models.IntegerField(null=True, blank=True)  # # Contrataciones
    # --- Talento9: Costo de contratación ---
    costo_contratacion = models.CharField(max_length=32, null=True, blank=True)  # $ Costo de contratación
    coste_reclutamiento_interno = models.CharField(max_length=32, null=True, blank=True)  # Coste reclutamiento interno
    coste_reclutamiento_externo = models.CharField(max_length=32, null=True, blank=True)  # Coste reclutamiento externo
    num_contrataciones_periodo = models.IntegerField(null=True, blank=True)  # # Contrataciones periodo
    # --- Talento10: Tasa de recuperación de incapacidades ---
    tasa_recuperacion_incapacidades = models.CharField(max_length=20, null=True, blank=True)  # % Tasa recuperación incapacidades
    incapacidades_radicadas_periodo = models.IntegerField(null=True, blank=True)  # Incapacidades radicadas por periodo
    incapacidades_para_cobro_periodo = models.IntegerField(null=True, blank=True)  # Incapacidades para cobro periodo
    # --- SST1: Consolidado ---
    num_siniestros_viales = models.IntegerField(null=True, blank=True)  # # Siniestros viales
    dato_numerador_sv = models.FloatField(null=True, blank=True)  # Dato Numerador SV (tn)*K
    dato_denominador_km = models.FloatField(null=True, blank=True)  # Dato Denominador km (t)
    # --- Seguridad1: Novedades viales vehículos ---
    porcentaje_novedades_viales = models.CharField(max_length=20, null=True, blank=True)  # % Novedades
    vehiculos_con_novedad = models.IntegerField(null=True, blank=True)  # # Vehículos con novedad
    vehiculos_programados = models.IntegerField(null=True, blank=True)  # # Vehículos programados
    # --- Seguridad2: Inspecciones a instalaciones ---
    porcentaje_cumplimiento_instalaciones = models.CharField(max_length=20, null=True, blank=True)  # % cumplimiento
    sumatoria_incumplimiento = models.CharField(max_length=32, null=True, blank=True)  # Sumatoria de Incumplimiento total, Parcialmente cumplido, Se cumple totalmente
    calificacion_cumple_totalmente = models.IntegerField(null=True, blank=True)  # Calificación se cumple totalmente
    # --- Seguridad3: Excesos de velocidad ---
    num_vehiculos_exceso_velocidad = models.IntegerField(null=True, blank=True)  # # vehículos con excesos de velocidad
    total_vehiculos_mes = models.IntegerField(null=True, blank=True)  # Total de vehículos en el mes
    # --- Seguridad4: Novedades flota propia botones de pánico ---
    sin_novedad = models.IntegerField(null=True, blank=True)  # Sin novedad
    total_botones_panico_prueba = models.IntegerField(null=True, blank=True)  # Total botones de pánico por prueba
    conductores_accionan_boton_panico_evento_critico = models.IntegerField(null=True, blank=True)  # # Conductores que accionan botón de pánico por evento crítico
    # --- SST2: Consolidado ---
    costos_siniestros_viales = models.FloatField(null=True, blank=True)  # Costos Siniestros viales
    costos_directos_siniestros_viales = models.FloatField(null=True, blank=True)  # Costos directos de siniestros viales
    costos_indirectos_siniestros_viales = models.FloatField(null=True, blank=True)  # Costos indirectos de siniestros viales
    # --- SST3: Riesgos de Seguridad Vial Identificados ---
    riesgos_seguridad_vial = models.FloatField(null=True, blank=True)  # Riesgos de seguridad vial
    cantidad_riesgos_final_anio = models.IntegerField(null=True, blank=True)  # Cantidad de riesgos identificados al final del año
    cantidad_riesgos_inicio_anio = models.IntegerField(null=True, blank=True)  # Cantidad de riesgos identificados al inicio del año
    # --- SST4: Gestión de riesgos viales ---
    gestion_riesgos_viales = models.FloatField(null=True, blank=True)  # Gestión de riesgos viales
    cant_riesgos_valoracion_alta_final_anio = models.IntegerField(null=True, blank=True)  # Cant. Riesgos con valoración alta al final del año
    cant_riesgos_valoracion_alta_inicio_anio = models.IntegerField(null=True, blank=True)  # Cant. Riesgos con valoración alta al inicio del año
    # --- SST5: Cumplimiento Metas PESV ---
    cumplimiento = models.FloatField(null=True, blank=True)  # Cumplimiento (%)
    num_metas_alcanzadas = models.IntegerField(null=True, blank=True)  # # Metas alcanzadas
    num_total_metas_definidas = models.IntegerField(null=True, blank=True)  # # Total de metas definidas
    # --- SST6: Cumplimiento de actividades plan anual ---
    cumplimiento_actividades = models.FloatField(null=True, blank=True)  # Cumplimiento actividades (%)
    num_actividades_ejecutadas = models.IntegerField(null=True, blank=True)  # # Actividades ejecutadas
    num_total_actividades_programadas = models.IntegerField(null=True, blank=True)  # # Total de actividades programadas
        # --- SST7: Exceso jornadas laborales ---
    num_excesos_jornada = models.IntegerField(null=True, blank=True)  # # Excesos jornada diaria de trabajo (sst7)
    total_dias_trabajados = models.IntegerField(null=True, blank=True)  # # Total días trabajados por los conductores (sst7)

    # --- SST8: Cobertura programa de gestión velocidad empresarial ---
    num_vehiculos_incluidos = models.IntegerField(null=True, blank=True)  # # Vehículos incluidos programa de gestión de velocidad -Mes (sst8)
    num_vehiculos_utilizados = models.IntegerField(null=True, blank=True)  # # Vehículos utilizados para desplazamientos laborales-Mes (sst8)

    # --- SST9: Excesos Límite de Velocidad Laboral ELVL ---
    num_excesos_velocidad_laboral = models.IntegerField(null=True, blank=True)  # # Diario de desplazamientos laborales con exceso de velocidad-Mes (sst9)
    total_desplazamientos_laborales_mes = models.IntegerField(null=True, blank=True)  # # Total de desplazamientos laborales por mes (sst9)

    # --- SST10: Inspecciones Diarias Preoperacionales (IDP) ---
    num_vehiculos_inspeccionados_diariamente = models.IntegerField(null=True, blank=True)
    total_vehiculos_trabajan_diariamente = models.IntegerField(null=True, blank=True)

    # --- SST11: Cumplimiento plan mantenimiento preventivo de vehículos (CPMVh) ---
    num_actividades_mantenimiento_ejecutadas = models.IntegerField(null=True, blank=True)
    total_actividades_mantenimiento_programadas = models.IntegerField(null=True, blank=True)

    # --- SST12: Cobertura plan de formación en seguridad vial (CPF PESV) ---
    num_capacitaciones_ejecutadas = models.IntegerField(null=True, blank=True)
    total_capacitaciones_programadas = models.IntegerField(null=True, blank=True)

    # --- SST13: No Conformidades Auditoría Cerradas (NCAC) ---
    num_no_conformidades_gestionadas_cerradas = models.IntegerField(null=True, blank=True)
    num_no_conformidades_identificadas_analizadas = models.IntegerField(null=True, blank=True)

    # --- SST14: Frecuencia de Accidentalidad ---
    total_at_mes = models.IntegerField(null=True, blank=True)  # # Total de AT en el mes
    num_trabajadores_mes = models.IntegerField(null=True, blank=True)  # # De trabajadores en el mes

    # --- SST15: Severidad de accidentalidad ---
    dias_incapacidad_at_mes = models.IntegerField(null=True, blank=True)  # # Días incapacidad por AT en el mes
    dias_cargados_mes = models.IntegerField(null=True, blank=True)        # # Días cargados en el mes
    num_trabajadores_mes = models.IntegerField(null=True, blank=True)     # # Trabajadores en el mes

    # --- SST16: Proporción de accidentes de trabajo mortales en el año ---
    num_at_mortales_anio = models.IntegerField(null=True, blank=True)  # # De AT mortales en el año
    total_at_anio = models.IntegerField(null=True, blank=True)         # Total de AT en el año

    # --- SST17: Cumplimiento en la ejecución de alcoholimetrías ---
    num_pruebas_positivas = models.IntegerField(null=True, blank=True)  # # Pruebas positivas
    num_empleados = models.IntegerField(null=True, blank=True)          # # Empleados
    num_pruebas_realizadas = models.IntegerField(null=True, blank=True) # # Pruebas realizadas

    # --- SST18: Inspecciones de seguridad ---
    cantidad_novedades_locativas = models.IntegerField(null=True, blank=True)  # Cantidad de Novedades (Inspecciones Locativas)
    total_inspecciones_elaboradas = models.IntegerField(null=True, blank=True) # Total de inspecciones elaboradas

    # --- SST19: Cierre acciones inspecciones ---
    num_novedades_cerradas = models.IntegerField(null=True, blank=True)  # SST19: # de novedades cerradas
    num_novedades_reportadas = models.IntegerField(null=True, blank=True)  # SST19: # total de novedades reportadas

    # --- SST20: Cumplimiento de requisitos de estructura del SG-SST ---
    num_requisitos_establecidos = models.IntegerField(null=True, blank=True)  # SST20: # de requisitos establecidos
    num_total_requisitos = models.IntegerField(null=True, blank=True)  # SST20: # total de requisitos

    # --- SST21: Ejecución de Capacitación ---
    num_capacitaciones_ejecutadas_sst21 = models.IntegerField(null=True, blank=True)  # SST21: # de capacitaciones ejecutadas
    num_capacitaciones_programadas_sst21 = models.IntegerField(null=True, blank=True)  # SST21: # total de capacitaciones programadas

    # --- SST22: Ejecución plan trabajo anual SG-SST ---
    num_actividades_ejecutadas_sst22 = models.IntegerField(null=True, blank=True)  # SST22: # de actividades ejecutadas
    num_actividades_programadas_sst22 = models.IntegerField(null=True, blank=True)  # SST22: # total de actividades programadas

    # --- SST23: Cumplimiento notificación incidentes y reporte AT y EL ---
    num_incidentes_reportados_sst23 = models.IntegerField(null=True, blank=True)  # SST23: # Incidentes reportados oportunamente SST
    num_total_incidentes_sst23 = models.IntegerField(null=True, blank=True)  # SST23: # Total de incidentes ocurridos en el periodo

    # --- SST24: Prevalencia de la Enfermedad Laboral (EL) ---
    num_casos_el_sst24 = models.IntegerField(null=True, blank=True)  # SST24: # Casos nuevos y antiguos de EL en el año
    promedio_trabajadores_sst24 = models.IntegerField(null=True, blank=True)  # SST24: Promedio trabajadores en el año

    # --- SST25: Incidencia de la Enfermedad Laboral (EL) ---
    num_casos_nuevos_el_sst25 = models.IntegerField(null=True, blank=True)  # SST25: # Casos nuevos Enfermedad Laboral en el año
    promedio_trabajadores_sst25 = models.IntegerField(null=True, blank=True)  # SST25: Promedio de trabajadores en el año

    # --- SST26: Ausentismo por causa médica ---
    num_dias_ausencia_sst26 = models.IntegerField(null=True, blank=True)  # SST26: # de días de ausencia por incapacidad laboral o común
    num_dias_trabajo_programados_sst26 = models.IntegerField(null=True, blank=True)  # SST26: # de días de trabajo programados
    num_trabajadores_sst26 = models.IntegerField(null=True, blank=True)  # SST26: # de trabajadores
    dias_laborados_mes_sst26 = models.IntegerField(null=True, blank=True)  # SST26: días laborados mes


    def __str__(self):
        # Representación legible del indicador en el admin
        return f"{self.submenu} - {self.periodo} {self.mes or ''}"

    def clean(self):
        # Validaciones personalizadas al guardar
        if not self.submenu:
            raise ValidationError('El campo "submenu" es obligatorio.')
        if not self.periodo:
            raise ValidationError('El campo "periodo" es obligatorio.')
        if self.porcentaje is None:
            raise ValidationError('El campo "porcentaje" es obligatorio.')

    def save(self, *args, **kwargs):
        # Llama a clean antes de guardar
        self.clean()
        super().save(*args, **kwargs)

# --- Modelo para almacenar la meta de cada submenú ---
class Meta(models.Model):
    # Identificador único del submenú
    submenu = models.CharField(max_length=100, unique=True)
    # Valor numérico de la meta
    valor = models.FloatField()
    # Tipo de meta: mayor, menor o igual
    tipo = models.CharField(max_length=10, choices=[('mayor', '>'), ('menor', '<'), ('igual', '=')])
    # Descripción textual de la meta
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        # Representación legible de la meta en el admin
        return f"{self.submenu}: {self.descripcion}"
