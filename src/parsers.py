def a_booleano(cadena:str)->bool:
    res = None
    if cadena.strip() == "win" or cadena.strip() == "1":
        res = True
    elif cadena.strip() == "loss" or cadena.strip() == "0":
        res = False
    return res

def parser(cadena:str)->list[str]:
    #res = list()
    #for elemento in cadena.split(','):
    #    res.append(elemento.strip())
    #return res
    return [elemento.strip() for elemento in cadena.split(',')]

def check_valor(cadena:str)->int:
    #res = None
    #if cadena == '':
    #    return res
    #else:
    #    res = int(cadena)
    #return res
    return None if cadena == '' else int(cadena)