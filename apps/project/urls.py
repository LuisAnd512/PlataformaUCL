from django.urls import path
from . import views
from apps.project.views import EdView, IndexView, EschuView, CPView , CCView, CNetView, EdCView,AccView,EdNetView,EdACCView,CAccView,DataView,EdDataView,CDataView,NetView

app_name = 'project'

urlpatterns = [
   path('', IndexView.as_view(), name ='index'),
   path('edicionProyectos/<id>', EdView.as_view(), name ='edicionProyectos'),
   path('Schudele/edicionCronogramas/<id>', EdCView.as_view(), name ='edicionCronogramas'),
   path('Schudele/Account/edicionAcc/<id>', EdACCView.as_view(), name ='edicionAcc'),
   path('Network/', NetView.as_view()),
   path('creacionNet', CNetView.as_view()),
   path('Network/edicionNet/<id>', EdNetView.as_view()),
   path('Schudele/Account/Data/edicionData/<id>', EdDataView.as_view()),
   path('creacionProyectos', CPView.as_view(), name ='creacionProyectos'),
   path('registrarNet/', views.registrarNet),
   path('Schudele/<id>', EschuView.as_view(), name ='Schedule/'),
   path('Schudele/Account/<id>', AccView.as_view(), name ='Schedule/'),
   path('Schudele/Account/Data/<id>', DataView.as_view()),
   path('creacionCronograma/<abc>', CCView.as_view(), name ='creacionCronograma'),
   path('creacionAcc/<abc>', CAccView.as_view(), name ='creacionAcc'),
   path('creacionData/<abc>', CDataView.as_view(), name ='creacionData'),
   path('creacionCronograma/registrarCronograma/',views.registrarCronograma),
   path('creacionAcc/registrarAcc/',views.registrarAcc),
   path('creacionData/registrarData/',views.registrarData),
   path('registrarProyecto/',views.registrarProyecto, name="registrarProyecto"),
   path('eliminacionProyectos/<id>', views.eliminacionProyectos),
   path('edicionProyectos/editarProyecto/',views.editarProyecto),
   path('Schudele/edicionCronogramas/editarCronograma/', views.editarCronograma),
   path('Schudele/Account/edicionAcc/editarAcc/', views.editarAcc),
   path('Network/edicionNet/editarNet/', views.editarNet),
   path('Schudele/Account/Data/edicionData/editarData/', views.editarData),
   path('Schudele/eliminacionSchudele/<id>', views.eliminacionSchudele),
   path('Schudele/Account/eliminacionAcc/<id>', views.eliminacionAcc),
   path('Network/eliminacionNet/<id>', views.eliminacionNet),
   path('Schudele/Account/Data/eliminacionData/<id>', views.eliminacionData)
]