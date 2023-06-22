from ClaseManejadorEmpleados import arrNumpy



def opcion0(mAL,mMa):
    print('ADIOS!!!')

def opcion1(mAL,mMa):
    print('Ingrese el DNI del Alumno a consultar')
    dni=int(input())
    
    promedio=mMa.promedio(dni)

    if promedio!=-1:
        print('EL promedio sin aplasos del alumno es: {}',promedio )
    else: print('no se encontro el alumno')


def opcion2(mAL, mMa):

    print('opcion2 ')
    

switcher = {
    0: opcion0,
    1: opcion1,
    2: opcion2
}
def switch(argument,mv,indice):
    func = switcher.get(argument, lambda: print("Opción incorrecta"))
    func(mv,indice)

if __name__=='__main__':
    cantempl=int(input("Ingrese la cantidad de empleados: "))
    aEm=arrNumpy(5,cantempl)
    aEm.testcontratados()
    aEm.testexternos()
    aEm.testplanta()

    aEm.mostrarDatos()


