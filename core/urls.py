from django.urls import path
from . import views

urlpatterns = [
    # path("",), #Localhost:p/empresa/agregar
    path("",views.index,name='empresa_agregar'),
    path("",views.restart,name='reset'),



]
