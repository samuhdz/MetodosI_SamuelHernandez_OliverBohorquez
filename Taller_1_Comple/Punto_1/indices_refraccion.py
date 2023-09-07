import numpy as np
import matplotlib.pyplot as plt
import os
import glob

def tuplas (archivo):
    arreglo=[]
    centinela=False
    datos=open(str(archivo),"r")
    linea=datos.readline()
    while centinela == False:
        linea=datos.readline()
        if "data: |" in linea:
            while linea != "" and centinela == False:
                linea=datos.readline().strip()
                lista=linea.split(" ")
                try:
                    float(lista[0])
                except ValueError:
                    centinela = True
                if linea != "" and centinela == False:
                    tupla=(lista[0],lista[1])
                    arreglo.append(tupla)
            centinela = True
    arreglo=np.array(arreglo,dtype=[('longitud_onda', float), ('indice_refraccion', float)])
    datos.close()
    return arreglo

print(tuplas("Taller_1_Comple/Punto_1/Vidrio/BF1.yml"))

def crear_grafico (archivo):
    arraytuplas=tuplas(archivo)
    nombre = os.path.splitext(os.path.basename(archivo))[0]
    x=[]
    y=[]
    n=0
    for i in arraytuplas:
        x.append(i[0])
        y.append(i[1])
        n+=i[1]
    ejex=(np.array(x))
    ejey=(np.array(y))
    npromedio=round(n/len(arraytuplas),3)
    desvest=round(np.std(ejey),3)
    fig,axs = plt.subplots(figsize=(6,4.5))
    axs.scatter(ejex,ejey,s=8)
    axs.set_ylabel('Índice de refracción - n')
    axs.set_xlabel('Longitud de onda - nm')
    axs.set_title(nombre + "\n n Promedio: " + str(npromedio) + " - Desviación estándar: " +str(desvest))
    fig.savefig(archivo.replace(".yml",".png"))
    return axs

KaptonRuta= "Taller_1_Comple/Punto_1/Plásticos Comerciales/Kapton.yml"
NOA1348Ruta="Taller_1_Comple/Punto_1/Adhesivos Ópticos/NOA1348.yml"

crear_grafico(KaptonRuta)
plt.show()
crear_grafico(NOA1348Ruta)
plt.show()



def crear_imagenes_graficas():
    rutas=glob.glob("**/*.yml", recursive=True)
    #no tengo muy claro el por qué el glob no me coge todas las rutas yml de todas las carpetas a pesar de haberle
    #pasado el **/*
    for i in rutas:
        crear_grafico(i)
        plt.close()
crear_imagenes_graficas()