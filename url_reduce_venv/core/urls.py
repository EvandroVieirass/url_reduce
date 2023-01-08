from . import views
from django.urls import path,include

urlpatterns = [
    path('',views.home, name='home'),
    path('valida_link',views.valida_link, name='valida_link'),
    path('<str:link>',views.redirecionar, name='redirecionar')
]