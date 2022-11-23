from django.shortcuts import render
from .models import lNum
# Create your views here.
def muestraDatos(request):
    consulta=lNum.objects.all()
    listSuma=calSuma(consulta)
    contexto=zip(consulta, listSuma)
    return render(request,'exam1/index.html',{'contexto':contexto})

def pagina():
    return render('exam1/navar.html')

def calSuma(l):
    listaSuma=[ ]
    for i in l:
        r=i.x1+i.x3+i.x4
        listaSuma.append(r)
    return listaSuma