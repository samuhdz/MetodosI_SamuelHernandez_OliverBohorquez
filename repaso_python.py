import numpy as np
import matplotlib.pyplot as plt

#Matplotlib es una librería para hcer gráficas y más cositas. 
#Numpy también, pero con funciones y métodos númericos
g= .9,8
v_0= 10
y_0= 200
UnU=str("Tu eres cuck, yo god:v")
t=np.linspace(start=0,stop=8, num=30)
def posicion (y0,v0,a,t):
    return y0+v0*t+(1/2)*(t**2)
array_posición=posicion(y_0,v_0,g,t)

fig, axs = plt.subplots(nrows=1, ncols=3, figsize=(24,8))

axs[0].scatter(t,array_posición) #Recibe arrays del mismo tamaño
axs[0].set_xlabel('Tiempo (s)')
axs[0].plot(t,array_posición) #Hace lo mismo pero uninedo puntos con lineas
vector_aceleracion=np.tile(g,30) #Me crea un array con todas las entradas iguales
 #Una clase es es una plantilla para un objeto

lugar= "Zapatoca- Santander, Colombia"
lugar.split("-")[1].strip() 
   