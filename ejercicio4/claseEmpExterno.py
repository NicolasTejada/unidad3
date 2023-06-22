from CLaseEMpleado import Empleado

class EmpleadoExterno(Empleado):
    __tarea=""
    __fechaInicio=""
    __fechaFinalizacion=""
    __viatico=0.0
    __costoObra=0.0
    __seguro=0.0


    def __init__(self, dni, nombre, direccion, telefono, tarea, fechaInicio, fechaFinalizacion, viatico, costoObra, seguro):
        super().__init__(dni, nombre, direccion, telefono)
        self.__tarea=tarea
        self.__fechaInicio=fechaInicio
        self.__fechaFinalizacion=fechaFinalizacion
        self.__viatico=viatico
        self.__costoObra=costoObra
        self.__seguro=seguro

    def __str__(self):
            super().__str__()
            print('Tipo:Externo  Tarea: {}\n'.format(self.__tarea))
            
    def getSueldo(self):
        sueldo=self.__costoObra - self.__viatico - self.__seguro

        return sueldo