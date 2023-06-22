class Inscripcion:
    __fechaInscripcion:str
    __pago=bool
    __persona=object
    __taller=object


    def __init__(self, fechainscripcion, pago, persona, taller ):
        self.__fechaInscripcion=fechainscripcion
        self.__pago=pago
        self.__persona=persona
        self.__taller=taller
        pass

    