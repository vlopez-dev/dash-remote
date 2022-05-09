import threading
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render,redirect
from requests import Response, request
import winrm
from django.contrib import messages #import messages
from .models import Equipo
import time
from .forms import Equipoform

from rest_framework import viewsets
from .serializers import EquipoSerializer




Connected = False

def index(request):
    equipos = Equipo.objects.all()
    return render(request,"core/index.html",{'equipos':equipos})





def add_server(request,id_equipo=0):
    if request.method == "GET":
        if id_equipo == 0 :
            form = Equipoform()
        else:
            equipo = Equipo.objects.get(pk=id_equipo)

            form = Equipoform(instance=equipo)
        return render(request, 'core/agregar_server.html', {'form': form})
    else:
        if id_equipo == 0:
            print(id_equipo)
            form = Equipoform(request.POST)
            print(form)
        else:
            equipo = Equipo.objects.get(pk=id_equipo)
            form = Equipoform(request.POST,instance= equipo)
    if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'Agregado correctamente!.')

    return redirect('/home/')













def restart(request,id_equipo):
    equipo= Equipo.objects.get(pk=id_equipo)
    session = winrm.Session(equipo.direction, auth=('administrador','AMEC4m3c1962'),transport='ntlm')
    result = session.run_ps("ping 192.168.1.228")
    result=result.std_out
    print("estoy en reiniciando")
    messages.success(request, "Equipo reiniciado." )
    return render(request,"core/index.html")





def poweroff(request,id_equipo):
    equipo=Equipo.objects.get(pk=id_equipo)
    print("estoy en poweroff")
    session = winrm.Session(equipo.direction, auth=('administrador','AMEC4m3c1962'),transport='ntlm')
    result = session.run_ps("ping 192.168.1.228")
    result=result.std_out
    messages.success(request, "Equipo Apagado." )

    return render(request,"core/index.html")



# def free_memory(request,id_equipo):
#     equipo=Equipo.objects.get(pk=id_equipo)
#     session = winrm.Session(equipo.direction, auth=('administrador','AMEC4m3c1962'),transport='ntlm')
#     result = session.run_ps("wmic OS get FreePhysicalMemory")
#     datasub=result.std_out.decode('UTF-8')
#     datalist = [int(i) for i in datasub.split() if i.isdigit()]
#     data=""
#     for i in datalist:
#         data=+i

#     data = {

#              'memoria': data,
#             }
#     return JsonResponse(data)



# def processor_consumption(request,id_equipo):
#         equipo=Equipo.objects.get(pk=id_equipo)
#         session = winrm.Session(equipo.direction, auth=('administrador','AMEC4m3c1962'),transport='ntlm')
#         result = session.run_ps("wmic cpu get loadpercentage")
#         datasub=result.std_out.decode('UTF-8')

#         datalist = [int(i) for i in datasub.split() if i.isdigit()]
#         data=""
#         for i in datalist:
#             data=+i


        
#         data = {

#              'procesador': data,
#             }
#         return JsonResponse(data)






def mem_pro_consum(id_equipo):
        equipo=Equipo.objects.get(pk=id_equipo)
        session = winrm.Session(equipo.direction, auth=('administrador','AMEC4m3c1962'),transport='ntlm')
        resultmemory = session.run_ps("wmic OS get FreePhysicalMemory")
        datasub=resultmemory.std_out.decode('UTF-8')
        datalist = [int(i) for i in datasub.split() if i.isdigit()]
        memoryfree=""
        for i in datalist:
            memoryfree=+i

        # proc consum
        resultproc = session.run_ps("wmic cpu get loadpercentage")
        datasub=resultproc.std_out.decode('UTF-8')
        datalist = [int(i) for i in datasub.split() if i.isdigit()]
        procons=""
        for i in datalist:
            procons=+i
        print(memoryfree)
        print(procons)
        ob= Equipo.objects.get(id_equipo=id_equipo)
        ob.memory_free=memoryfree
        ob.pro_consum=procons
        
        ob.save()
        # return render(request,"core/index.html")




class EquipoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Equipo.objects.all().order_by('id_equipo')
    serializer_class = EquipoSerializer

    
    def get(self, request, id_equipo):
        equipo = get_object_or_404(Equipo, pk=id_equipo)
        serializer = EquipoSerializer(equipo)
        print(serializer)
        return Response({'serializer': serializer, 'equipo': equipo})























def get_value():
    while Connected != True:  # Wait for connection
        time.sleep(3)
        ob = Equipo.objects.all()
        for i in ob:
                mem_pro_consum(i.id_equipo)  





sub = threading.Thread(target=get_value)
sub.start()
