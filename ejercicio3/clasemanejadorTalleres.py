import csv 

import numpy as np

from claseTallerCapacitacion import taller


class arregloNumPy:
    __cantidad:0
    __dimension:0
    __incremento:5


    def __init__(self, dimension, incremento):
        self.__talleres=np.empty(dimension, dtype=taller)
        self.__cantidad=0
        self.__dimension=dimension

        pass

    def agregarTaller(self, unTaller):
        if self.__cantidad==self.__dimension:
                self.__dimension+=self.__incremento
                self.__talleres.resize(self.__dimension)
        self.__talleres[self.__cantidad]=unTaller
        self.__cantidad+=1
        