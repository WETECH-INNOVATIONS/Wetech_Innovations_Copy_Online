from django.contrib import admin
from Apps.usuario.models import *
# from eav.forms import BaseDynamicEntityForm
# from eav.admin import BaseEntityAdmin


# # Register your models here.
# admin.site.register(Usuario)

# class UsuarioAdminForm(BaseDynamicEntityForm):
#     model = Usuario

# class UsuarioAdmin(BaseEntityAdmin):
#     form = UsuarioAdminForm

# class model_pruebaForm(BaseDynamicEntityForm):
#     model = model_prueba

# class model_pruebaAdmin(BaseEntityAdmin):
#     form = model_pruebaForm

admin.site.register(Usuario)#,UsuarioAdmin)
admin.site.register(model_prueba)#,model_pruebaAdmin)
