from django.shortcuts import render
from exam1.models import lNum
from django.http import HttpResponse
#from statistics import  pvariance
import math
import random
from numpy import mean, var, exp
#import numpy as np
#import seaborn as sns
#import matplotlib.pyplot as plt
def algBay(request):
    return render(request, 'exam3/alg3.html')
def algoritmo_cbi(request):
    bd = list(lNum.objects.all())
    new_bd = lNum.objects.values('x2','x1','x3','x4').order_by('x2')
    letra=[]
    bd_final={}
    probabilidad=""
    cont=0
    for i in range(len(new_bd)):
        # si la letra no esta en el arreglo que haga esto, si no ignorar
        if bd[i].x2 in letra:
            cont+=1
        else:
            valor = lNum.objects.filter(x2=bd[i].x2)
            letra.append(bd[i].x2)
            suma_num1=[]
            suma_num3=[]
            suma_num4=[]
            for j in list(valor):
                suma_num1.append(j.x1)
                suma_num3.append(j.x3)
                suma_num4.append(j.x4)
            media_num1=mean(suma_num1)
            varianza_num1= var(suma_num3)
            media_num3=mean(suma_num3)
            varianza_num3=var(suma_num3)
            media_num4=mean(suma_num4)
            varianza_num4=var(suma_num4)
            bd_final[bd[i].x2]=(media_num1,varianza_num1,media_num3,varianza_num3,media_num4,varianza_num4)
    para_evidencia = {}
    if request.method == 'POST':
        x = int(request.POST['x'])
        y = int(request.POST['y'])
        z = int(request.POST['z'])
        p_letra = 1/len(bd_final)
        for l in range(len(bd_final)):
            para_evidencia[letra[l]]= pre_posteriori(bd_final[letra[l]][0],bd_final[letra[l]][2],bd_final[letra[l]][4],bd_final[letra[l]][1],bd_final[letra[l]][3],bd_final[letra[l]][5],x,y,z)

        evidcia = evidencia(para_evidencia,letra,p_letra)
        probabilidad = post_posteriori(para_evidencia,evidcia,letra)
        cont = {'letra': probabilidad}
    else:
        return render(request, 'exam3/alg3.html', {})
    return render(request, 'exam3/alg3.html', cont)
def pre_posteriori(media1,media3,media4,var1,var2,var3,x,y,z):
    var1 = random.randint(1, 10)
    var2 = random.randint(1, 10)
    var3 = random.randint(1, 10)
    p_num1 = (1/math.sqrt(2*math.pi*var1))* math.e*(pow(x-media1,2)/(2*var1))
    p_num3 = (1/math.sqrt(2*math.pi*var2))* math.e*(pow(y-media3,2)/(2*var2))
    p_num4 = (1/math.sqrt(2*math.pi*var3))* math.e*(pow(z-media4,2)/(2*var3))
    return (p_num1,p_num3,p_num4)

def post_posteriori(para_evidencia, evidencia,letras):
    rel = {}
    valores_rel =[]
    letra=""
    for i in range(len(para_evidencia)):
        val = (para_evidencia[letras[i]][0]*para_evidencia[letras[i]][1]*para_evidencia[letras[i]][2]) / evidencia
        rel[letras[i]]= val
        valores_rel.append(val)
    maximo = max(valores_rel) 
    keys = list(rel.keys())  
    for j in range(len(rel)):
        if rel[letras[j]] == maximo:
            letra = keys[j]
    return letra
def evidencia(para_evidencia,letras,p_letra):
    rel=[]
    for i in range(len(para_evidencia)):
        rel.append(p_letra*para_evidencia[letras[i]][0]*para_evidencia[letras[i]][1]*para_evidencia[letras[i]][2])
    resultado = sum(rel)
    return resultado

def calcular_varianza(arr, is_sample=False):
    media = (sum(arr) / len(arr))
    diff = [(v - media) for v in arr]
    sqr_diff = [d**2 for d in diff]
    sum__sqr_diff = sum(sqr_diff)

    if is_sample == True:
        variance = sum__sqr_diff/(len(arr)-1)
    else:
        variance = sum__sqr_diff/(len(arr)-1)
    return variance
