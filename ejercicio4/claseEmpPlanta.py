from CLaseEMpleado import Empleado


class EmpPlanta(Empleado):
    __sueldoBasico=0.0
    __antiguedad=0


    def __init__(self, dni, nombre, direccion, telefono, sueldoBasico, antiguedad):
        super().__init__(dni, nombre, direccion, telefono)
        self.__sueldoBasico=sueldoBasico
        self.__antiguedad=antiguedad

    def __str__(self):
        super().__str__()
        print('Tipo:Planta  Antiguedad:{}\n'.format(self.__antiguedad))
    
        

    def getSueldo(self):
        
        sueldo= self.__sueldoBasico + (self.__sueldoBasico*0.01)*self.__antiguedad

        return sueldo
     