import csv 

from claseHelado import Helado

class ManejadorHelados:
    __helados=[]

    def __init__(self):
        self.__helados=[]
        pass


    def agregarHelado(self, unHelado):
        self.__helados.append(unHelado)

    
    def testHelado(self, gramos, precio, sabores):
        cantidad=len(sabores)
        unHelado=Helado(gramos,precio,cantidad, sabores)

