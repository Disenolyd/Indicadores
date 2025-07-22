from django.contrib import admin
from .models import Indicador
from django.contrib.auth.models import User
from .models import Meta

# Register your models here.
admin.site.register(Indicador)
admin.site.register(Meta)

class UserAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=None):
        # No permitir eliminar el superusuario
        if obj and obj.is_superuser:
            return False
        return super().has_delete_permission(request, obj)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
