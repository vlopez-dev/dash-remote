from django.shortcuts import render,redirect
import winrm
from django.contrib import messages #import messages
from .models import Equipo

from .forms import Equipoform

def index(request):
    equipos = Equipo.objects.all()
    return render(request,"core/index.html",{'equipos':equipos})




def restart(request):

    session = winrm.Session('192.168.1.206', auth=('administrador','AMEC4m3c1962'),transport='ntlm')
    result = session.run_ps("ping 192.168.1.228")
    result=result.std_out
    messages.success(request, "Equipo reiniciado." )
    return render(request,"core/index.html")





def poweroff(request):

    session = winrm.Session('192.168.1.206', auth=('administrador','AMEC4m3c1962'),transport='ntlm')
    result = session.run_ps("ping 192.168.1.228")
    result=result.std_out
    messages.success(request, "Equipo apagado." )

    return render(request,"core/index.html")



def free_memory(request):
    session = winrm.Session('192.168.1.206', auth=('administrador','AMEC4m3c1962'),transport='ntlm')
    result = session.run_ps("wmic OS get FreePhysicalMemory")

    resultado=result.std_out.decode('UTF-8')
    print(resultado)



def processor_consumption(request):
        session = winrm.Session('192.168.1.206', auth=('administrador','AMEC4m3c1962'),transport='ntlm')
        result = session.run_ps("wmic cpu get loadpercentage")

        resultado=result.std_out.decode('UTF-8')
        print(resultado)
        
        
        
        



def add_server(request, id_equipo=0):

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

        
