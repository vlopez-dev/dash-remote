from django.http import JsonResponse
from django.shortcuts import render,redirect
import winrm
from django.contrib import messages #import messages
from .models import Equipo

from .forms import Equipoform

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



def free_memory(request,id_equipo):
    equipo=Equipo.objects.get(pk=id_equipo)
    session = winrm.Session(equipo.direction, auth=('administrador','AMEC4m3c1962'),transport='ntlm')
    result = session.run_ps("wmic OS get FreePhysicalMemory")
    datasub=result.std_out.decode('UTF-8')
    datalist = [int(i) for i in datasub.split() if i.isdigit()]
    data=""
    for i in datalist:
        data=+i

    data = {

             'memoria': data,
            }
    return JsonResponse(data)



def processor_consumption(request,id_equipo):
        equipo=Equipo.objects.get(pk=id_equipo)
        session = winrm.Session(equipo.direction, auth=('administrador','AMEC4m3c1962'),transport='ntlm')
        result = session.run_ps("wmic cpu get loadpercentage")
        datasub=result.std_out.decode('UTF-8')

        datalist = [int(i) for i in datasub.split() if i.isdigit()]
        data=""
        for i in datalist:
            data=+i


        
        data = {

             'procesador': data,
            }
        return JsonResponse(data)