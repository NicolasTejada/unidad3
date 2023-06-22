class Sabor:
    __idSabor= int
    __ingredientes=""
    __nombre=""
    
    @classmethod
    def getIdSabor(cls):
        cls.__idSabor+=1
        return cls.__idSabor

    def __init__(self, ingredientes, nombre):
        self.__ingredientes=ingredientes
        self.__nombre=nombre

        pass
    def getId(self):
        return self.__idSabor
    def getNombre(self):
        return self.__nombre