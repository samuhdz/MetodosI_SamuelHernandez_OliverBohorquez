
import numpy as np


archivo = 'minerales.txt'
datos_por_fila = {}

with open(archivo, 'r', encoding='utf-8') as fi:
    for i, linea in enumerate(fi, start=1):
        
        datos = linea.strip().split('\t')
        

        datos_por_fila[i] = datos

import mineral as mi
from mineral import Mineral



def crear_objetos (datos):
    objetos_minerales=np.array([])
    for i in range (1,len(datos)):
        mineral_i=Mineral(datos[i][0],datos[i][1],datos[i][2],datos[i][3],datos[i][4],datos[i][5],datos[i][6],datos[i][7],)
        if mineral_i not in objetos_minerales:
            objetos_minerales=np.append(objetos_minerales,mineral_i)
        else:
            objetos_minerales=objetos_minerales

    return objetos_minerales

def numero_silicatos (objetos):
    objects=crear_objetos(objetos)
    numero=0
    for i in objects:
        if i.silicato()==True:
            numero+=1
    return numero
def densidad_promedio (objetos):
    objects=crear_objetos(objetos)
    objects_1=objects[1:]
    densidad=[]
    for i in objects_1:
        densidad.append(i.densidad())

    
    return np.mean(densidad)










