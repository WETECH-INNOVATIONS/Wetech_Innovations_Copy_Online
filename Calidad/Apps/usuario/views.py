from django.shortcuts import render
from django.http import JsonResponse
from Apps.usuario.models import *
from django.http import HttpResponse
from dynamic_models.models import ModelSchema, FieldSchema
# Create your views here.

def getUsuario(request):
    users = Usuarios.objects.all()
    data = list(users.values("id","nombre","fechaCreacion"))
    return JsonResponse(data, safe=False)

def getUsuarioDetail(request, param):
    data = Usuarios.objects.filter(id=param)
    return JsonResponse(list(data.values("id","nombre","fechaCreacion")),safe=False)

def prueba_modelo(request):
    carr_schema = ModelSchema.objects.create(name='modelonuevo6')
    modelonuevo6 = carr_schema.as_model()
    modelonuevo6.objects.create()

    car_model_field = FieldSchema.objects.create(model_schema=carr_schema, name='modelo', data_type='character', null=True)
    car_year_field = FieldSchema.objects.create(model_schema=carr_schema, name='anio', data_type='integer', null=True)
    Car = carr_schema.as_model()
    Car.objects.create(modelo='Camry', anio=1997)
    return HttpResponse("esquema")
    
