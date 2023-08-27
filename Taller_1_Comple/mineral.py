# %%
class Mineral:
    def __init__(self,nombre,dureza,rompimiento_por_fractura,color,composicion, lustre,specific_gravity, sistema_cristalino,):
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
            silicato1=True
        else:
            silicato1=False
        return self.silicato
    def densidad (self):
        return str((self.specific_gravity)*(997))+"kg/m^3"
    def mostrar_color(self):
         
        fig, ax = plt.subplots()

        
        ax.set_facecolor(self.color)
        ax.set_title('Color más frecuente de'+self.nombre)
        plt.show()
    def es_por_fractura (self):
        rompimiento=" "
        if self.rompimiento_por_fractura==True:
            rompimiento=" por fractura"
        else:
            rompimiento=" no es por fractura"
        return rompimiento
    def imprimir (self):
        print("La dureza del material es:"+ str(self.dureza)+  " , su tipo de rompimiento es" + es_por_fractura(self)+ "y el sistema de los átomos es "+ self.sistema_cristalino )



