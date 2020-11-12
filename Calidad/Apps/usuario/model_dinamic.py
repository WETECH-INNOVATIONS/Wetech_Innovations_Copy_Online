# from django.db import models
# from django.db.models.loading import cache

# class model_base(models.Model):
#     tipo_campo = models.CharField('Tipo de Campo',max_length=30)
#     class Meta:
#         abstract = True

# class model_abstracto(model_base):
    
#     try:
#         del cache.app_models[usuario][model_base]
#     except KeyError:
#         pass

#     attrs = {
#         'name': models.CharField(max_length=32),
#         '__module__': 'usuario.model_dinamic'
#     }
#     Proceso = type("Proceso", (models.Model,), attrs)
