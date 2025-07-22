# Sistema de Indicadores TIC y Registros

## ¿Qué hace este sistema?
- Visualiza en tiempo real indicadores y registros de 9 áreas, con submenús y datos actualizados desde la base de datos.
- Cada submenú muestra una tabla y una gráfica de barras, con colores que indican si se cumplen las metas.
- Permite descargar reportes PDF anuales y mensuales (según el submenú).
- Solo usuarios con correos permitidos pueden acceder.

## Seguridad y gestión de usuarios
- **Solo existe un superusuario administrador** (creado con `createsuperuser`).
- **Solo el superusuario puede acceder al panel de administración** (`/admin`).
- **El superusuario puede crear, editar y cambiar contraseñas** de los usuarios permitidos (los de `ALLOWED_EMAILS`).
- **El superusuario puede editar su propia información** (nombre, correo, contraseña).
- **El superusuario no puede ser eliminado** desde el admin (protegido por código).
- **No crees más superusuarios ni usuarios staff** para mantener la seguridad centralizada.
- Los usuarios normales solo pueden iniciar sesión y visualizar indicadores si su correo está en `ALLOWED_EMAILS` y tienen una contraseña válida.

## Flujo de uso
1. **Inicio de sesión:** Solo los correos autorizados pueden acceder.
2. **Menú lateral:** Selecciona la categoría y submenú que deseas consultar.
3. **Visualización:**
   - Tabla y gráfica se llenan automáticamente con los datos de la base de datos.
   - Las celdas de porcentaje se pintan de rojo claro si no cumplen la meta.
   - Los datos se actualizan en tiempo real al modificar la base de datos.
4. **Reportes PDF:** Descarga el reporte anual o mensual (según el submenú) con un solo clic.
5. **Cerrar sesión:** Usa el botón de logout para salir de forma segura.

## Estructura de datos (modelo Indicador)
- **Campos generales:** periodo, mes, porcentaje, tickets_cerrados, tickets_abiertos_hardware, tickets_abiertos_software
- **Campos específicos por submenú TIC:** total_copias_realizadas, total_copias_seguridad_exitosa, ataques_ciberseguridad, total_equipos, porcentaje_fallas_seguridad, porcentaje_cumplimiento_programa, mantenimientos_programados, total_mantenimientos_realizados

## Metas de cumplimiento (color rojo si no se cumple):
- **TIC 1:** % Fallas > 85
- **TIC 2:** % Fallas > 95
- **TIC 3:** % Fallas == 0
- **TIC 4:** % Cumplimiento > 90

## Dependencias principales
- Django
- matplotlib
- reportlab
- openpyxl (opcional, para futuras importaciones desde Excel)

## Cómo actualizar los datos
- Modifica la base de datos directamente (admin de Django, shell, script SQL, etc.).
- Los cambios se reflejan automáticamente en la web.

## Despliegue
1. Instala las dependencias con:
   ```
   pip install -r requirements.txt
   ```
2. Aplica migraciones:
   ```
   python manage.py migrate
   ```
3. Corre el servidor:
   ```
   python manage.py runserver
   ```

## Notas sobre usuarios y contraseñas
- Los usuarios válidos son los correos definidos en la lista `ALLOWED_EMAILS` en `views.py`.
- Las contraseñas corresponden a los usuarios creados en el sistema Django (puedes crearlos desde el admin o con el comando `createsuperuser`).
- Si necesitas crear usuarios con correo y contraseña específicos, usa el admin de Django o el shell:
   ```python
   from django.contrib.auth.models import User
   User.objects.create_user(username='correo@ejemplo.com', email='correo@ejemplo.com', password='tu_contraseña')
   ```
- **Solo el superusuario puede cambiar contraseñas y gestionar usuarios.**
- **El superusuario no puede ser eliminado desde el admin.**

## Notas adicionales
- Los correos permitidos están definidos en la lista `ALLOWED_EMAILS` en `views.py`.
- Las contraseñas corresponden a los usuarios creados en el sistema Django (puedes crearlos desde el admin o con el comando `createsuperuser`).
- Si necesitas crear usuarios con correo y contraseña específicos, usa el admin de Django o el shell:
   ```python
   from django.contrib.auth.models import User
   User.objects.create_user(username='correo@ejemplo.com', email='correo@ejemplo.com', password='tu_contraseña')
   ``` 