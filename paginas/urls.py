from django.urls import path

from . import views

urlpatterns = [
    path('', views.index , name='index'),
    path('nosotros/', views.nosotros , name='index'),
    path('contacto/', views.contacto , name='contacto'),
    path('login/', views.login , name='login'),
    path('signup/', views.signup , name='signup'),
    path('sorry/', views.sorry , name='sorry'),
    path('producto/', views.producto , name='producto'),
    path('vendedor/', views.vendedor , name='vendedor'),
    # path('', views.listadoSQL , name='listadoSQL'),
]
