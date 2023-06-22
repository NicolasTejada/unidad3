class Helado:
    __gramos=0.00
    __precio=0.00
    __sabores=[]

    def __init__(self, gramos, precio, cantidad, sabor=None):
        self.__gramos=gramos
        self.__precio=precio
        if sabor==None and cantidad <= 3:
            for i in range(cantidad):
                self.addSabor(sabor[i])

        pass


    def addSabor(self, sabor):
        self.__sabores.append(sabor)