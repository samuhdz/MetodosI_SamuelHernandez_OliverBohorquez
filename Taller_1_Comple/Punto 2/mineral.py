
import numpy as np
import matplotlib.pyplot as plt

class Mineral:
    def __init__(self,nombre,dureza,rompimiento_por_fractura,color,composicion, lustre,specific_gravity, sistema_cristalino):
        self.nombre=nombre
        self.dureza=dureza
        self.lustre=lustre
        self.rompimiento_por_fractura=rompimiento_por_fractura
        self.color=color
        self.composicion=composicion
        self.sistema_cristalino=sistema_cristalino
        self.specific_gravity=specific_gravity
    def silicato (self):
        silicato=True
        if "Si" in self.composicion and "O" in self.composicion:
            silicato=True
        else:
            silicato=False
        return silicato 
    def densidad (self):
        decimal_gravedad=float(self.specific_gravity)
        return decimal_gravedad*(997) 
    def mostrar_color(self):
         # Crear una figura y un eje
        fig, ax = plt.subplots()

        # Establecer el color de fondo
        ax.set_facecolor(self.color)
        ax.set_title('Color de'+self.nombre)
        plt.show()
    def es_por_fractura (self):
        rompimiento=" "
        if self.rompimiento_por_fractura=="TRUE":
            rompimiento=" por fractura"
        else:
            rompimiento=" no es por fractura"
        
        return rompimiento
    def imprimir (self):
        print("La dureza del material es:"+ str(self.dureza)+  " , su tipo de rompimiento es" + self.es_por_fractura()+ " y el sistema de los átomos es "+ self.sistema_cristalino )






