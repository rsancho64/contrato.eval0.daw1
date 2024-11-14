#! /usr/bin/python3

def canonic(s):
    return s.lower().strip()

if __name__ == "__main__":

    dicc = {}
    print(dicc)

    # uso el diccionario como un conjunto
    dicc["nombre"] = "" 
    dicc["apellido1"] = "sancho"

    # UNA forma canonica de una cadena
    # 1. no tiene espacios en blanco en head nor tail
    # 2. todo minusculas

    s = [
        "ramon",
        "  Ramon",    
        "Ramon   ",
        "RaMOn",        
        "rAmon",
        "",
    ]


    for item in s:
        print(item.lower().strip())
        print(canonic(item))

