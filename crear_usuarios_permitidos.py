from django.contrib.auth import get_user_model

# Lista de correos permitidos
ALLOWED_EMAILS = [
    'juan.alvarez@design.com.co',
    'sofia.garcia@design.com.co',
    'andres.guzman@design.com.co',
    'vamos.design@gmail.com',
]

PASSWORDS = {
    'juan.alvarez@design.com.co': 'TemporalJuan2024!',
    'sofia.garcia@design.com.co': 'TemporalSofia2024!',
    'andres.guzman@design.com.co': 'TemporalAndres2024!',
    'vamos.design@gmail.com': 'TemporalVamos2024!',
}

User = get_user_model()

# Eliminar usuarios que no están en la lista permitida
for user in User.objects.all():
    # Usar getattr para evitar errores de linter si el modelo personalizado no tiene email
    user_email = getattr(user, 'email', None)
    if user_email not in ALLOWED_EMAILS:
        print(f"Eliminando usuario: {user_email}")
        user.delete()

# Crear o actualizar los usuarios permitidos
for email in ALLOWED_EMAILS:
    password = PASSWORDS[email]
    user, created = User.objects.get_or_create(email=email, defaults={'username': email})
    user.set_password(password)
    user.save()
    if created:
        print(f"Usuario creado: {email}")
    else:
        print(f"Usuario actualizado: {email}")
print("Listo. Solo existen los 4 usuarios permitidos con contraseñas temporales.") 