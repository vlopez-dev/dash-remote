from django.urls import path,include
from rest_framework import routers

from . import views



router = routers.DefaultRouter()
router.register(r'equipo', views.EquipoViewSet)

urlpatterns = [
    path("home/",views.index,name='home'),

    path('<int:id_equipo>/restart',views.restart,name='restart'),
    path('<int:id_equipo>/',views.delete_server,name='delete'),

    path('<int:id_equipo>/poweroff',views.poweroff,name='poweroff'),
    path("addserver/",views.add_server,name='add_server'),
    path("<int:id_equipo>/sendmessage",views.send_message,name='sendmessage'),


    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))


]
