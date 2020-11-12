from django.db import models
import eav
from dynamic_models.models import ModelSchema, FieldSchema


# # Create your models here.
class Usuario(models.Model):
  nombre = models.CharField(max_length=200)
  fechaCreacion = models.DateField()
  nivel = models.IntegerField(default=0) 

# # class model_abstracto(models.Model):
# #   try:
# #     del cache.app_models[usuario][model_abstracto]
# #   except KeyError:
# #     pass

# # attrs = {
# #   'name': models.CharField(max_length=32),
# #   '__module__': 'usuario.model_dinamic'
# # }
# # Proceso = type("Proceso", (models.Model,), attrs)

# eav.register(Usuario)

class model_prueba(models.Model):
  name = models.CharField('nombre model prueba',max_length=30, default =  "wilmer")
  descrips = models.CharField('descripcion',max_length=30, default =  "escriba su descripcion")

# eav.register(model_prueba)


class Userr(models.Model):
  email = models.EmailField('email')
  name = models.CharField(max_length=100, null=True, blank=True)

