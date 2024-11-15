#! /usr/bin/python3

# from marvelous import rainbow

import collections.abc
class monton():
 
    stuff = [] 
    
    def __init__(self, *args):
        """init regular y de copia"""
        self.stuff = []
        for item in args:
            self.amontona(item)
 
    def __str__(self)-> str:
        """doc..."""
        answ = "<<"
        for item in self.stuff:
            answ += f"{str(item)}, "
        answ += ">>"
        return answ
    
    def amontona(self, algo):
        """ si algo no es monton,, al monton
        si algo es monton, todo lo que tiene, al monton
        """
        if isinstance(algo, monton):
            self.stuff.extend(algo.stuff)
        else:
            self.stuff.append(algo)

    def __contains__(self, algo):
        return algo in self.stuff

    def copiar(self, algo) -> object:
        if algo in self.stuff:
            return algo
        return None # todo raise ValueError

    def tomar(self, algo) -> object:
        if algo in self.stuff:
            self.stuff.remove(algo)
            return algo
        return None  # todo raise ValueError

if __name__ == "__main__":
    
    m0 = monton()        # m0 es un nuevo monton vacio
    print("m0: ", m0)

    m2 = monton("mas","tomas")        # m0 es un nuevo monton vacio
    print("m2: ", m2)

    m3 = monton(11,"doce",13)        # m0 es un nuevo monton vacio
    print("m3: ", m3)

    m4 = monton(11,"doce",13,m2)        # m0 es un nuevo monton vacio
    print("m4: ", m4)

    mOirig = monton("mas","tomas")        # m0 es un nuevo monton vacio
    print("mOrig: ", mOirig)

    mCopia = monton(mOirig)
    print("mCopia: ", mCopia)

    myset = set()
    myset.add(22)
    myset.add(33)
    print(33 in myset)
    
    myMonton = monton()
    myMonton.amontona(22)
    myMonton.amontona(33)
    print(33 in myMonton)

    exit(0) # ==ir bajando...===========================

    m1.amontona("perla")
    # assert: en m1 hay "algo" y "algo mas" y "perla" y NADA MAS.
    print("m1: ", m1)

    m1.amontona("y mas mierdas")
    # assert: en m1 hay ...
    print("m1: ", m1)


    # puedo amontonar -todo lo que haya- en un monton 
    # en otro moton.
    # Esto no vacia el monton argumentado (m1 aqui)
    # Esto no vacia previamente el monton invocado (m0 aqui)
    # no ~ m0 = m1
    m0.amontona(m1)

    predicado = m0.contiene("perla") # predicado == True
    copia = m0.copiar("perla") # copia == "perla"
    tesoro = m0.tomar("perla") # tesoro == "perla" ; en m0 DESAPARECE la "perla"
   

    