from django.urls import path
from . import views

urlpatterns = [
    path('', views.fooldal, name='fooldal'),
    path('rolunk/', views.rolunk), 
    path('uj_szemely/', views.uj_szemely, name="uj_szemely"),
]
