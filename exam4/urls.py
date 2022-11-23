from django.urls import path
from . import views
urlpatterns = [
    path('exam4/', views.regLog, name='Reglineal'),
]