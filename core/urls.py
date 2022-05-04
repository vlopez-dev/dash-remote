from django.urls import path
from . import views

urlpatterns = [
    # path("",), #Localhost:p/empresa/agregar
    path("home/",views.index,name='home'),
    path("restart/",views.restart,name='restart'),
    path("poweroff/",views.poweroff,name='poweroff'),
    path("addserver/",views.add_server,name='add_server'),


]
