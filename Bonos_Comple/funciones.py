import numpy as np

def posicion(A,k,m,t):
    '''
    Esta función retorna la posición, x, en un tiempo de de una masa m atada a un
    resorte de constante de fuerza k que inicialmente es desplazada A unidades de
    su posición de equilibrio. Esta función devuelve el resultado de 

    $A\sin (\omega t)$ donde $\omega = \sqrt{\frac{k}{m}}$

    Parámetros
    ----------
    A: float
        La amplitud o desplazamiento inicial de la masa.
    k: float
        La constante de fuerza del resorte.
    m: float
        La masa del objeto.
    t: float
        El tiempo en el cual se quiere calcular la posición.
    '''
    omega = np.sqrt(k/m)
    return A*np.sin(omega*t)


t=np.linspace(0,14,100)
h=t[1]-t[0]
def auxiliar (t):
    posicion=posicion(2,800,2,t)
    return posicion

def derivada_derecha (t,f,h):
    derivada=(f(t+h)-f(t))/h
    return derivada 
def derivada_izquierda (t,f,h):
    derivada=(f(t)-f(t-h))/h
    return derivada 
def derivada_central (t,f,h):
    derivada=(f(t+h)-f(t-h))/2*h
    return derivada 
def derivada_array(x,f_array,h=1):
    derivadas=[]
    for i in range(1,len(x)):
        derivada_i=(f_array[i-1]-f_array[i])/(x[i-1]-x[i])
        derivadas.append(derivada_i)
    return np.array(derivadas)

def metodo_biseccion (f,a,b):
    precision_1=0.0001
    c=(a+b)/2
    f_a=f(a)
    f_b=f(b)
    f_c=f(c)
    while f(c)>precision_1:
        if f_c<0:
            a=c

    
