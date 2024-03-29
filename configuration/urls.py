from django.urls import path,include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'configuration', views.SysemailViewSet)
urlpatterns = [
    path("configuration/",views.configuration,name='config_home'),
    path("add_config/",views.add_sysemail,name='add_config'),
    path("configcheck/",views.change_para,name='config_check'),
    # path("<int:id_param>/delete_param/",views.delete_parameter,name='delete_param'),


    path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))


]