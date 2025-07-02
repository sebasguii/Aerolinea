from django.shortcuts import render, redirect
from .models import Avion
from .forms import AvionForm, RegistroUsuariosForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

# Create your views here.

def home(request):
    #Renderiza la plantilla home
    return render(request, 'home.html')

#Registro usuarios

def registro(request):
    if request.method == 'POST':
        form = RegistroUsuariosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistroUsuariosForm()
    
    return render (request, 'registro.html', {'form' : form})

def iniciar_sesion(request):
    if request.method == 'POST':
        usuario = request.POST['username']
        clave = request.POST ['password']
        user = authenticate(request,username=usuario, password = clave)
        if user:
            login(request,user)
            return redirect('lista_Avion')
        
    return render(request,'login.html')
        
    # return render(request, 'login.html')

def cerrar_sesion(request):
    logout(request)
    return redirect('login')

@login_required
def lista_Avion(request):
    avion = Avion.objects.all()
    return render(request, 'Avion/lista.html', {'Aviones' : avion})

@login_required
def agregar_Avion(request):
    form = AvionForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_Avion')
    return render( request, 'Avion/form.html', {'form':form})

@login_required
def editar_Avion(request,id):
    avion =  Avion.objects.get(id=id)
    form = AvionForm(request.POST or None, instance=avion)
    if form.is_valid():
        form.save()
        return redirect('lista_Avion')
    else:
        return render( request, 'Avion/form.html', {'form':form})



@login_required

def eliminar_Avion(request, id):
    avion = Avion.objects.get(id=id)
    avion.delete()
    return redirect('lista_Avion')

@login_required
def generar_reporte_pdf(request):
    avion = Avion.objects.all()  # Usa otro nombre para la variable
    template_path = 'Avion/reporte_pdf.html'
    context = {'avion': avion}  # Corrige el nombre en el contexto

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="reporte_aviones.pdf"'

    template = get_template(template_path)
    html = template.render(context)

    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('Hubo un error al generar el PDF', status=500)
    return response

@login_required
def dashboard_aviones(request):
    avion = Avion.objects.all()  # Usa otro nombre para la variable
    nombres = [a.modelo for a in avion]
    # Cambia 'precio' por un campo existente, por ejemplo 'id' o cualquier otro campo numérico
    datos = [a.id for a in avion]  # Reemplaza 'id' por el campo adecuado si existe

    return render(request, 'Avion/dashboard.html', {
        'labels': nombres,
        'data': datos
    })