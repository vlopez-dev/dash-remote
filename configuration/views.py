from django.shortcuts import render
from requests import Response
from configuration.serializer import ConfigurationSerializer

from core.models import Configuration

# Create your views here.

def configuration(request):
    return render(request,"configuration/config_home.html")







class ConfigurationViewSet(viewsets.ModelViewSet):

    queryset = Configuration.objects.all().order_by('id_configuration')
    serializer_class = ConfigurationSerializer
    template_name = 'core/index.html'


    def get(self, request, id_config):
        configuration = get_object_or_404(Equipo, pk=id_config)
        serializer = ConfigurationSerializer(configuration)
        print(serializer)
        return Response({'serializer': serializer, 'configuration': configuration},template_name='test.html')