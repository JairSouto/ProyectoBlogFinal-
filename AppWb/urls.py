import imp
from django.urls import path 
from AppWb import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
 
    path('', views.inicio, name='Inicio'),
    path('asociados',views.asociados, name='Asociados'),
    path('equipos', views.equipos, name='Equipos'),
    path('cursos',views.cursos, name='Cursos'),
    path('busquedaSeguidores', views.busquedaSeguidores, name='BusquedaSeguidores'),
    path('buscar/',views.buscar),
    path('leerCursos/', views.lecturaCursos, name='LecturaCursos'),
    path('eliminarCursos/<cursos_nombre>/',views.eliminarCurso,name='EliminarCursos'),
    path('editarCursos/<cursos_nombre>/',views.editarCurso, name='EditarCursos'),
    path('editarUsuario',views.editarUsuario,name='EditarUsuario'),

    path('curso/list', views.CursosList.as_view(), name='List'),

    path('login', views.login_request, name='Login'),
    path('register',views.register,name='Register'),
    path('logout', LogoutView.as_view(template_name='AppWb/logout.html'),name='Logout'),
    





    path(r'^(?P<pk>\d+)$', views.CursosDetalle.as_view(), name='Detail'),
    path(r'^nuevo$',views.CursosCreacion.as_view(), name='New'),
    path(r'^editar/(?P<pk>\d+)$',views.CursosUpdate.as_view(), name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$',views.CursosDelete.as_view(), name='Delete'),
    ]

