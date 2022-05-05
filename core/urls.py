from django.urls import path
from . import views

urlpatterns = [
    path("home/",views.index,name='home'),
    path('<int:id_equipo>/',views.restart,name='restart'),
    path('<int:id_equipo>/',views.poweroff,name='poweroff'),
    path("addserver/",views.add_server,name='add_server'),
    path("free_memory/<int:id_equipo>",views.free_memory,name='free_memory'),


]
