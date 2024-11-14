#! /usr/bin/python3

# from marvelous import rainbow

from canonic import canonic

class monton():

    # __name__
    __stuff = "" # PARA MASOCAS
    
    def __init__(self, *args: ...):
        """doc..."""
        self.__stuff = ",".join(args)

    def __str__(self)-> str:
        """doc..."""
        return f"<<{self.__stuff}>>"

    # " .. "  <- " .., .., ..."
    # " .. "  <- obj
    
    def amontona(self, algo):
        """doc..."""
        if isinstance(algo, monton):
            if self.__stuff:
                self.__stuff += "," + algo.__stuff
                # print(algo)
            else:
                self.__stuff = algo.__stuff
        else:
            palabra = canonic(str(algo))
            if self.__stuff:
                self.__stuff += "," + palabra
                # print(palabra)                            
            else:
                self.__stuff = palabra

    def contiene(self, algo) -> bool:
        """doc..."""
        palabra = str(algo)
        numero_perlas = self.__stuff.count(palabra)
        if numero_perlas >= 1:
            # print(numero_perlas)
            return True
        else:
            # print("no pearls")
            return False

    def copiar(self, algo) -> object:
        """doc..."""
        palabra = str(algo)
        num_perlas = 0
        if palabra in self.__stuff:
            num_perlas = self.__stuff.count(palabra)
            print(num_perlas)
            return palabra
        else:
            print("no pearls")
            return None


    def tomar(self, algo) -> object:
        """doc..."""
        palabra = str(algo)
        num_perlas = 0
        if palabra in self.__stuff:
            num_perlas = self.__stuff.count(palabra)
            self.__stuff = self.__stuff.replace(palabra,'',num_perlas)
            self.__stuff = self.__stuff.replace(",,",',',num_perlas)
            print(num_perlas)
            return palabra
        else:
            print("no pearls")
            return None

if __name__ == "__main__":
    
    m0 = monton()        # m0 es un nuevo monton vacio
    print(m0)

    m1 = monton("algo","algo mas")  # m0 es un nuevo monton con "algo"
    # m1.amontona("algo mas")
    # assert: en m1 hay "algo" y "algo mas" y NADA MAS.
    print(m1)
    
    m1.amontona("perla")
    print(m1)    
    # assert: en m1 hay "algo" y "algo mas" y "perla" y NADA MAS.

    m1.amontona("y mas mierdas")
    # assert: en m1 hay ...
    print(m1)        

    # puedo amontonar -todo lo que haya- en un monton 
    # en otro moton.
    # Esto no vacia el monton argumentado (m1 aqui)
    # Esto no vacia previamente el monton invocado (m0 aqui)
    # no ~ m0 = m1
    m0.amontona(m1)
    print(m0)

    predicado = m0.contiene("perla") # predicado == True
    print(predicado)

    copia = m0.copiar("perla") # copia == "perla"
    print(copia)

    tesoro = m0.tomar("perla") # tesoro == "perla" ; en m0 DESAPARECE la "perla"
    print(m0)  
  

    exit(0) # ==ir bajando...===========================

    
    
    