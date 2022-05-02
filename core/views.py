from django.shortcuts import render
import winrm

from .models import Equipo

# Create your views here.
def index(request):
    equipos = Equipo.objects.all()
    return render(request,"core/index.html",{'equipos':equipos})






def comprobar_estado(request):
    session = winrm.Session('192.168.1.206', auth=('administrador','AMEC4m3c1962'),transport='ntlm')
    result = session.run_ps("")
    print(result.std_out)
    
    
def restart(request):
    session = winrm.Session('192.168.1.206', auth=('administrador','AMEC4m3c1962'),transport='ntlm')
    result = session.run_ps("")
    mensaje=("Listo")
    print(result.std_out)
    return render(request,"core/index.html",mensaje)