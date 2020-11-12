from django.urls import path
from Apps.usuario.views import *

urlpatterns = [
    path('', getUsuario),
    path('<int:param>/', getUsuarioDetail),
    path('prueba_modelo/', prueba_modelo, name="prueba_modelo"),
]