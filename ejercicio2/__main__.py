from ClaseManejadorHelados import ManejadorHelados

from ClaseManejadorsabores import manejadorSabores


def opcion0(mHe,mSab):
    print('ADIOS!!!')

def opcion1(mHe,mSab):
    gramos=input("Ingrese el gramaje del Helado  ")
    canSabores=int(input("Ingrese la cantidad de sabores del pote como maximo 3"))
    sabores=[]
    for i in range(canSabores):
        sclave= input("Ingrese el sabor a buscar")
        sabor= mSab.getSabor(sclave)

        sabores.append(sabor)
    
    mHe.testHelado(gramos, 1000, sabores)

    print('Se registro la venta del Helado correctamente')

def opcion2(mAL, mMa):

  print('opcion 2')

switcher = {
    0: opcion0,
    1: opcion1,
    2: opcion2}
def switch(argument,mv,indice):
    func = switcher.get(argument, lambda: print("Opción incorrecta"))
    func(mv,indice)



if __name__=='__main__':

    mHe=ManejadorHelados()
    mSab= manejadorSabores()
    mSab.testSabores()
    

    bandera = False
    while not bandera:
        print("\nMENU DE OPCIONES")
        print("0 Salir")
        print("1- Registrar Helado")
        print("2- opcion 2")
        opcion = int(input ('Ingrese una opcion:'))
        switch(opcion, mHe , mSab)
        bandera = int(opcion)== 0

    