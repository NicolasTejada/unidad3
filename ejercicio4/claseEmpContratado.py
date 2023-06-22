from CLaseEMpleado import Empleado


class EmpContratado(Empleado):
    __fechaInicio=""
    __fechaFinalizacion=""
    __cantidadHoras=0
    __valorHora=0.0

    
    def __init__(self, dni, nombre, direccion, telefono, fechaInicio, fechaFinalizacion, horas, valorHora):
        super().__init__(dni, nombre, direccion, telefono)
        self.__fechaFinalizacion=fechaFinalizacion
        self.__fechaInicio=fechaInicio
        self.__cantidadHoras=horas
        self.__valorHora=valorHora

    def __str__(self):
        super().__str__()
        print('Tipo: Contratado  Fecha Finalizacion\n'.format(self.__fechaFinalizacion))

    def getsueldo(self):
        sueldo=self.__cantidadHoras*self.__valorHora

        return sueldo
    
    