import numpy as np

import csv 

from CLaseEMpleado import Empleado

from claseEmpContratado import EmpContratado

from claseEmpExterno import EmpleadoExterno

from claseEmpPlanta import EmpPlanta

class arrNumpy:
    __cantidad=0
    __incremento=5
    __dimension=0


    def __init__(self,dimension, incremento=5):
        self.__Empleados= np.empty(dimension, dtype=Empleado)
        self.__cantidad=0
        self.__dimension=dimension
        pass
    
    def mostrarDatos(self):
        for i in range(self.__cantidad):
            print(self.__Empleados[i])


    def agregarEmpleado(self, unEmpleado):
        if self.__cantidad==self.__dimension:
            self.__dimension+=self.__incremento
            self.__Empleados.resize(self.__dimension)
        
        self.__Empleados[self.__cantidad]=unEmpleado
        self.__cantidad+=1
        

    def testplanta(self):
        archivo= open('ejercicio4\planta.csv')
        reader=csv.reader(archivo, delimiter=';')

        for fila in reader:
            dni=fila[0]
            nombre=fila[1]
            domicilio=fila[2]
            telefono=fila[3]
            sueldo=fila[4]
            antiguedad=fila[5]

            unEmpleado=EmpPlanta(dni,nombre,domicilio,telefono,sueldo,antiguedad)
            self.agregarEmpleado(unEmpleado)
        archivo.close()

    def testexternos(self):
        archivo= open('ejercicio4\externos.csv')
        reader=csv.reader(archivo, delimiter=';')

        for fila in reader:
            dni=fila[0]
            nombre=fila[1]
            domicilio=fila[2]
            telefono=fila[3]
            obra=fila[4]
            inicio=fila[5]
            finalizacion=fila[6]
            viatico=fila[7]
            precio=fila[8]
            seguro=fila[9]
            
            unEmpleado=EmpleadoExterno(dni,nombre,domicilio,telefono,obra,inicio,finalizacion,viatico,precio,seguro)
            self.agregarEmpleado(unEmpleado)
        archivo.close()

    def testcontratados(self):

        archivo= open('ejercicio4\contratados.csv')
        reader=csv.reader(archivo, delimiter=';')

        for fila in reader:
            dni=fila[0]
            nombre=fila[1]
            domicilio=fila[2]
            telefono=fila[3]
            inicio= fila[4]
            finalizacion=fila[5]
            horas=fila[6]
            precioHora=fila[7]

            unEmpleado=EmpContratado(dni,nombre,domicilio,telefono,inicio,finalizacion,horas, precioHora)
            self.agregarEmpleado(unEmpleado)

            
        archivo.close()

    
            



