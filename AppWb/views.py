


from django.http import HttpResponse
from django.shortcuts import render
from AppWb import forms
from django.contrib.auth.models import User

from AppWb.forms import EquiposFormularios, AsociadosFormularios, CursosFormularios, UserRegisterForm
from AppWb.models import Asociados, Avatar, Cursos, Equipos
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
 #LOGIN
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.mixins import LoginRequiredMixin





@login_required
def editarUsuario(request):
    usuario=request.user
    if request.method == 'POST':
        miFormulario = UserRegisterForm(request.POST)

      

        if miFormulario.is_valid():
            
            informacion=miFormulario.cleaned_data

            usuario.username = informacion['username']
            usuario.email=informacion['email']
            usuario.password1=informacion['password1']
            usuario.password2=informacion['password2']

            usuario.save()
            return render(request, 'AppWb/inicio.html')
    else: 
        miFormulario= UserRegisterForm(initial={'username':usuario.username, 'email': usuario.email})
    return render(request, 'AppWb/editarUsuario.html', {'miFormulario':miFormulario, 'username':usuario.username})

def register(request):
    if request.method=='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username= form.cleaned_data['username']
            form.save()
            return render(request,'AppWb/inicio.html', {'mensaje': "UsuarioCreado"})
    else:
        form= UserRegisterForm()
    return render(request, 'AppWb/registro.html',{'form':form})





def login_request(request):
    if request.method =='POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            usuario=form.cleaned_data.get('username')

            contraseña=form.cleaned_data.get('password')

            user=authenticate(username=usuario, password=contraseña)

            if user:
                login(request, user)
                return render(request, 'AppWb/inicio.html', {'mensaje':f"Bienvenido {user}"})
        else:

            return render(request, 'AppWb/inicio.html',{'mensaje':"Error. Datos incorrectos"})
    else:
        form=AuthenticationForm()
    return render(request, 'AppWb/login.html',{'form':form})
        

# Create your views here.

def inicio(request):
    return render(request,'AppWb/inicio.html')
def About(request):
    return render(request,'AppWb/about.html')
@login_required
def asociados(request):
    if request.method=='POST':
        miFormulario= AsociadosFormularios(request.POST)
        print(miFormulario)


        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data

            asociados=Asociados(nombre=informacion['nombre'], redes_sociales=informacion['redes_sociales'])
            asociados.save()

            return render(request,"AppWb/inicio.html")
    else:
        miFormulario= AsociadosFormularios()
    return render(request,'AppWb/asociados.html', {'miFormulario':miFormulario})



@login_required
def cursos(request):
   
    if request.method=='POST':
        miFormulario= CursosFormularios(request.POST)
        print(miFormulario) 


        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data

            cursos=Cursos(nombre=informacion['nombre'], jugadorpro=informacion['jugadorpro'], duracion=informacion['duracion'])
            cursos.save()

            return render(request,"AppWb/inicio.html")
    else:
        miFormulario= CursosFormularios()
    return render(request,'AppWb/cursos.html', {'miFormulario':miFormulario})
@login_required
def equipos(request):
    if request.method=='POST':
        miFormulario= EquiposFormularios(request.POST)
        print(miFormulario)


        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data

            equipos=Equipos(nombre=informacion['nombre'], seguidores=informacion['seguidores'],)
            equipos.save()

            return render(request,"AppWb/inicio.html")
    else:
        miFormulario= EquiposFormularios()
    return render(request,'AppWb/equipos.html', {'miFormulario':miFormulario})

def busquedaSeguidores(request):
    return render(request, 'AppWb/busquedaSeguidores.html')

@login_required
def buscar(request):
    if request.GET['seguidores']:
        seguidores=request.GET['seguidores']
        equipos=Equipos.objects.filter(seguidores__icontains=seguidores)
        return render(request, "AppWb/resultadoBusqueda.html",{'equipos':equipos, 'seguidores':seguidores})
   # respuesta =f"Estoy este numero de seguidores :{request.GET['seguidores']}"#
    else:
        respuesta ="No enviaste Datos"
        return HttpResponse(respuesta)
@login_required
def lecturaCursos(request):
    cursos=Cursos.objects.all()
    contexto1= {'cursos':cursos}
    return render(request, 'AppWb/lecturaCursos.html', contexto1)

def lecturaEquipos(request):
    equipos=Equipos.objects.all()
    contexto3= {'equipos':equipos}
    return render(request, 'AppWb/lecturaEquipos.html', contexto3)

@login_required
def eliminarCurso(request, cursos_nombre):

    cursos=Cursos.objects.get(nombre=cursos_nombre)
    cursos.delete()
    
    cursos= Cursos.objects.all()
    contextin= {'cursos': cursos}
    return render(request, 'AppWb/lecturaCursos.html', contextin)

@login_required
def editarCurso(request,cursos_nombre):
    cursos=Cursos.objects.get(nombre=cursos_nombre)
    if request.method == 'POST':
        miFormulario = CursosFormularios(request.POST)

        print(miFormulario)

        if miFormulario.is_valid():
            
            informacion=miFormulario.cleaned_data

            cursos.nombre = informacion['nombre']
            cursos.jugadorpro=informacion['jugadorpro']
            cursos.duracion=informacion['duracion']

            cursos.save()
            return render(request, 'AppWb/inicio.html')
    else: 
        miFormulario= CursosFormularios(initial={'nombre':cursos.nombre, 'jugadorpro': cursos.jugadorpro, 'duracion': cursos.duracion})
    return render(request, 'AppWb/editarCurso.html', {'miFormulario':miFormulario, 'cursos_nombre':cursos_nombre})


class CursosList( LoginRequiredMixin  ,ListView):
    model = Cursos
    template_name = 'AppWb/curso_list.html'
class CursosDetalle(LoginRequiredMixin  ,DetailView):
    model = Cursos
    template_name = 'AppWb/cursos_detalle.html'
class CursosCreacion(LoginRequiredMixin  , CreateView):
    model = Cursos
    success_url = '/AppWb/curso/list'
    fields = ['nombre', 'jugadorpro','duracion']
class CursosUpdate( LoginRequiredMixin  ,UpdateView):
    model = Cursos
    success_url = '/AppWb/curso/list'
    fields = ['nombre', 'jugadorpro','duracion']
class CursosDelete(LoginRequiredMixin ,DeleteView):
    model = Cursos
    success_url = '/AppWb/curso/list'


