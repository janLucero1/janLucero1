from django.urls import path
from .import views

urlpatterns = [
    path('exam2/', views.algKNN_list, name='algKNN'),
   
]