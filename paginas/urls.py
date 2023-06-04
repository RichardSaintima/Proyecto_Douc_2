from django.urls import path

from . import views

urlpatterns = [
    path('', views.index , name='index'),
    path('nosotros/', views.nosotros , name='nosotros'),
    path('contacto/', views.contacto , name='contacto'),
    path('login/', views.login_v , name='login'),
    path('signup/', views.signup , name='signup'),
    path('sorry/', views.sorry , name='sorry'),
    path('producto/', views.producto , name='producto'),
    path('comprar/<int:pk>/', views.comprar , name='comprar'),
    path('verificaCompra', views.verificaCompra , name='verificaCompra'),
    path('crear', views.crear, name='crear'),
    path('eliminar/<str:pk>', views.eliminar, name='eliminar'),
    path('actualizar/<str:pk>', views.actualizar, name='actualizar'),
    path('productoUpdate/<int:pk>/', views.productoUpdate, name='productoUpdate'),
    path('vendedor/', views.vendedor , name='vendedor'),
    path('logout/', views.logout_v, name='logout'),
]
