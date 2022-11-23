from django.urls import path
from .import views

urlpatterns = [
    path('exam1/', views.muestraDatos, name='exam1'),
   
]