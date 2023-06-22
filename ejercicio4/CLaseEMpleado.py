class Empleado:
    __DNI:0
    __nombre=""
    __direccion=""
    __telefono=""

    def __init__(self, dni, nombre, direccion, telefono ):
        self.__DNI=dni
        self.__nombre=nombre
        self.__direccion=direccion
        self.__telefono=telefono

        pass


    def __str__(self):
        cadena='EMPLEADO: \n'
        cadena+= 'DNI:{}, Nombre:{}'.format(self.__DNI, self.__nombre)
        return cadena
        pass