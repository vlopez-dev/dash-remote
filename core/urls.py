from django.urls import path,include
from rest_framework import routers

from . import views



router = routers.DefaultRouter()
router.register(r'equipo', views.EquipoViewSet)

urlpatterns = [
    path("home/",views.index,name='home'),
    path('<int:id_equipo>/',views.restart,name='restart'),
    path('<int:id_equipo>/',views.poweroff,name='poweroff'),
    path("addserver/",views.add_server,name='add_server'),

    # path("server_values/<int:id_equipo>",views.mem_pro_consum,name='server_values'),

    path('home/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))


]
