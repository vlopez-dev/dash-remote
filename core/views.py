from distutils.command.clean import clean
import json
import threading
from django.http import HttpResponseBadRequest, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render,redirect
from requests import Response, request
import requests
import winrm
from django.contrib import messages #import messages
from .models import Equipo
import time
import datetime
from .forms import Equipoform, Mensajeform

from rest_framework import viewsets
from .serializers import EquipoSerializer




Connected = False

def index(request):
    equipos = Equipo.objects.all()
    return render(request,"core/index.html",{'equipos':equipos})





def add_server(request,id_equipo=0):
    print(request.method)
    if request.method == "GET":
        if id_equipo == 0 :
            form = Equipoform()
        else:
            equipo = Equipo.objects.get(pk=id_equipo)

            form = Equipoform(instance=equipo)
        return render(request, 'core/agregar_server.html', {'form': form})
    else:
        if id_equipo == 0:
            form = Equipoform(request.POST)
        else:
            equipo = Equipo.objects.get(pk=id_equipo)
            form = Equipoform(request.POST,instance= equipo)
    if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'Agregado correctamente!.')

    return redirect('/home/')




def delete_server(request,id_equipo):
    equipo = Equipo.objects.get(pk=id_equipo)
    equipo.delete()
    messages.add_message(request, messages.INFO, 'Eliminado correctamente!.')

    return redirect('/home')









def restart(request,id_equipo):
    equipo= Equipo.objects.get(pk=id_equipo)
    admin=equipo.user_admin.format()
    passw=equipo.passwordadmin.format()
    session = winrm.Session(equipo.direction, auth=(admin,passw),transport='ntlm')
    result = session.run_ps("ping 192.168.1.228")
    result=result.std_out
    print("estoy en reiniciando")
    messages.success(request, "Equipo reiniciado." )
    return redirect('/home')





def poweroff(request,id_equipo):
    print("estoy apagando el equipo......")
    equipo=Equipo.objects.get(pk=id_equipo)
    admin=equipo.user_admin.format()
    passw=equipo.passwordadmin.format()
    print("estoy en poweroff")
    session = winrm.Session(equipo.direction, auth=(admin,passw),transport='ntlm')
    result = session.run_ps("ping 192.168.1.228")
    result=result.std_out
    messages.success(request, "Equipo Apagado." )

    return redirect('/home')







def mem_pro_consum(id_equipo):
        equipo=Equipo.objects.get(pk=id_equipo)
        admin=equipo.user_admin.format()
        passw=equipo.passwordadmin.format()
        session = winrm.Session(equipo.direction, auth=(admin,passw),transport='ntlm')
        resultmemory = session.run_ps("wmic OS get FreePhysicalMemory")
        datasub=resultmemory.std_out.decode('UTF-8')
        datalist = [int(i) for i in datasub.split() if i.isdigit()]
        memoryfree=""
        for i in datalist:
            memoryfree=+i

        resultproc = session.run_ps("wmic cpu get loadpercentage")
        datasub=resultproc.std_out.decode('UTF-8')
        datalist = [int(i) for i in datasub.split() if i.isdigit()]
        procons=""
        for i in datalist:
            procons=+i
        if memoryfree and procons ==None:
            state=False
        else:
            state=True
        print(procons)
        print(state)
        equipo.state=state
        roundgb=memoryfree/1000/1024
        mem_free_round=round(roundgb)
        print(mem_free_round)
        equipo.memory_free=mem_free_round
        equipo.pro_consum=procons
        equipo.save()



def send_message(request,id_equipo):
<<<<<<< HEAD
        form = Mensajeform()

        if request.method == "GET":
            form = Mensajeform()

            return render(request, 'core/send.html', {'form': form})
        else:
            form = Mensajeform(request.POST)
            


        return redirect('/home/')

=======
   
>>>>>>> b9ae797bafff0f433f6ef57189b44c5eba2a23da




class EquipoViewSet(viewsets.ModelViewSet):

    queryset = Equipo.objects.all().order_by('id_equipo')
    serializer_class = EquipoSerializer
    template_name = 'core/index.html'


    def get(self, request, id_equipo):
        equipo = get_object_or_404(Equipo, pk=id_equipo)
        serializer = EquipoSerializer(equipo)
        print(serializer)
        return Response({'serializer': serializer, 'equipo': equipo},template_name='test.html')




def get_value():
    while Connected != True:  # Wait for connection
        time.sleep(150)
        ob = Equipo.objects.all()
        for i in ob:
                mem_pro_consum(i.id_equipo)  





sub = threading.Thread(target=get_value)
sub.start()



