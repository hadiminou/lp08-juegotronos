def a_booleano(cadena:str)->bool:
    res = True
    if cadena.strip() == "win" or cadena.strip() == "1":
        return res
    elif cadena.strip() == "loss" or cadena.strip() == "0":
        res = False
    return res

def parser(cadena:str)->list[str]:
    res = list()
    for elemento in cadena.split(','):
        res.append(elemento.strip())
    return res

def check_valor(cadena:str)->int:
    res = None
    if cadena == '':
        return res
    else:
        res = int(cadena)
    return res