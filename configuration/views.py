from ast import Param
from django.shortcuts import render,redirect
from requests import Response
from configuration.serializer import  SysemailSerializer
from rest_framework import viewsets
from .forms import ParameterForm, SysemailForm
from configuration.models import Sysemail
from .models import Sysemail,Parameter
import sweetify

# Create your views here.

def configuration(request):
    return render(request,"configuration/config_home.html")








def add_sysemail(request,id_config=0):
    if request.method == "GET":
        if id_config == 0 :
            form =SysemailForm()
        else:
            config = Sysemail.objects.get(pk=id_config)

            form = SysemailForm(instance=config)
        return render(request, 'configuration/add_config_email.html', {'form': form})
    else:
        if id_config == 0:
            form = SysemailForm(request.POST)
        else:
            config = Sysemail.objects.get(pk=id_config)
            form = SysemailForm(request.POST,instance= config)
    if form.is_valid():
            form.save()
            sweetify.success(request, 'Exito', text='Agregado Correctamente', persistent='Aceptar')


    return redirect('/configuration/configuration/')







def change_para(request,id_param=0):
        

    if request.method == "GET":
            if id_param == 0 :
                form =ParameterForm()
            else:
                param = Parameter.objects.get(pk=id_param)

                form = ParameterForm(instance=param)
            return render(request, 'configuration/configcheck.html', {'form': form})
    else:
            if id_param == 0:
                form = ParameterForm(request.POST)
            else:
                param = Parameter.objects.get(pk=param)
                form = ParameterForm(request.POST,instance= param)
    if form.is_valid():
                paramlast=Parameter.objects.last()
                paramlast.delete()
                form.save()
                sweetify.success(request, 'Exito', text='Agregado Correctamente', persistent='Aceptar')


    return redirect('/configuration/configuration/')







def delete_parameter(request,id_param):
    param = Parameter.objects.get(pk=id_param)
    param.delete()
    sweetify.success(request, 'Exito', text='Eliminado Correctamente', persistent='Aceptar')

    return redirect('/home')


def reset_config(request):
    param = Parameter.objects.latest()
    sysemail= Sysemail.objects.latest()
    param.delete()
    sysemail.delete()
    sweetify.success(request, 'Exito', text='Eliminado Correctamente', persistent='Aceptar')








class SysemailViewSet(viewsets.ModelViewSet):

    queryset = Sysemail.objects.all().order_by('id_config')
    serializer_class = SysemailSerializer
    template_name = 'core/index.html'


    def get(self, request, id_config):
        configuration = get_object_or_404(Equipo, pk=id_config)
        serializer = SysemailSerializer(configuration)
        print(serializer)
        return Response({'serializer': serializer, 'configuration': configuration},template_name='test.html')
