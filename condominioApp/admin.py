from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(RoleType)
admin.site.register(Condominio)
admin.site.register(Directivo)
admin.site.register(Empleado)
admin.site.register(Users)
admin.site.register(Edificios)
admin.site.register(Departamentos)
admin.site.register(Mantenimiento)
admin.site.register(Departamento_user)