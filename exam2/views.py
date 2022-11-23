from django.http import HttpResponse
from django.shortcuts import render
from exam1.models import lNum
import math

# Create your views here.
def algKNN_list(request):
    return render(request, 'exam2/navar.html')

def buscar(request):
    if request.GET["k"].isdigit() and request.GET["x1"].isdigit() and request.GET["x2"].isdigit() and request.GET["x3"].isdigit():
        k = int(request.GET["k"])
        x1 = int(request.GET["x1"])
        x2 = int(request.GET["x2"])
        x3 = int(request.GET["x3"])
        consulta = lNum.objects.all()
        listDist = calculaDist(consulta, x1, x2, x3)
        equivalente = varEquivalente(consulta)
        contexto = zip(listDist, equivalente)
        contexto = sorted(contexto)
        contado = contar(contexto, k)
        referencia = refe(contexto, contado, k)
        mensaje = referencia
        return render(request, 'exam2/navar.html', {'resultado': referencia})
    else:
        mensaje = "Error en los datos"
    return HttpResponse(mensaje)

def calculaDist(lista, x1, x2, x3):
    listaDist = []
    for i in lista:
        listaDist.append(round(math.sqrt(((x1 - i.x1)**2 + (x2 - i.x3)**2 + (x3 - i.x4)**2 )), 3))
    return listaDist

def varEquivalente(consulta):
    equivalente = []
    for x in consulta:
        equivalente.append(x.x2)
    return equivalente

def contar(contexto, k):
    contadores = []
    y = 0
    for dist, variable in contexto:
        if y < k:
            z = 0
            cont = 0
            for dist, band in contexto:
                if z < k:
                    if variable == band:
                        cont = cont + 1
                else:
                    break
                z = z + 1
            contadores.append(cont)
        else:
            break
        y = y + 1
    return contadores

def refe(contexto, contado, k):
    cont = 0
    maxi = 0 
    variable = ''
    for equiv, i in zip(contexto, contado):
        if i > maxi and cont < k:
            maxi = i
            variable = equiv[1]
        elif cont == k-1:
            break
        cont = cont + 1
    return variable     