import csv

from claseSabor import Sabor


class manejadorSabores:
    __listaSabores=[]

    def __init__(self):
        self.__listaSabores=[]

        pass
    def agregarSabor(self, unSabor):
        self.__listaSabores.append(unSabor)

    def getSabor(self, clave):
        i=0
        while self.__listaSabores[i].getNombre() != clave:
            i+=1
        return self.__listaSabores[i].getId()

    def testSabores(self):
        archivo=open('sabores.csv')
        reader=csv.reader(archivo, delimiter=';')

        for fila in reader:
            ingredientes= fila[0]
            nombre= fila[1]

            unSabor=Sabor(ingredientes, nombre)
            self.agregarSabor(unSabor)

