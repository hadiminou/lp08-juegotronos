from typing import*
import csv
from parsers import*
from collections import defaultdict

BatallaGOT = NamedTuple('BatallaGOT',
    [('nombre', str), ('rey_atacante', str), ('rey_atacado', str), ('gana_atacante', bool),
     ('muertes_principales', bool), ('comandantes_atacantes', List[str]), ('comandantes_atacados', List[str]),
     ('region', str), ('num_atacantes', Optional[int]), ('num_atacados', Optional[int])])

def lee_batallas(ruta_fichero:int)->List[Tuple[BatallaGOT]]:
    res = list()
    with open(ruta_fichero, 'rt', encoding = 'utf-8') as f:
        lector = csv.reader(f, delimiter = ',')
        next (lector)
        for nombre, rey_atacante, rey_atacado, gana_atacante, muertes_principales, comandantes_atacantes,\
            comandantes_atacados, region, num_atacantes, num_atacados in lector:
            gana_atacante = a_booleano(gana_atacante)
            muertes_principales = a_booleano(muertes_principales)
            comandantes_atacantes = parser(comandantes_atacantes)
            comandantes_atacados = parser(comandantes_atacados)
            num_atacantes = check_valor(num_atacantes)
            num_atacados = check_valor(num_atacados)
            res.append(BatallaGOT(nombre.strip(), rey_atacante.strip(), rey_atacado.strip(), gana_atacante,\
                    muertes_principales, comandantes_atacantes, comandantes_atacados,\
                        region.strip(), num_atacantes, num_atacados))
        return res
    
def reyes_mayor_menor_ejercito(batallas:list[BatallaGOT])->Tuple[str, str]:
    dic_reyes = defaultdict(int)
    for i in batallas:
        if i.num_atacantes != None:
            dic_reyes[i.rey_atacante]+=i.num_atacantes
        if i.num_atacados != None:
            dic_reyes[i.rey_atacado]+=i.num_atacados
    return (max(dic_reyes.items(), key = lambda x:x[1])[0], min(dic_reyes.items(), key = lambda x:x[1])[0])

def batallas_mas_comandantes(batallas:list[BatallaGOT], regiones:Optional[set[str]]=None,\
                            n_batallas:Optional[int]=None)->List[Tuple[str, int]]:
    dic_batalla = defaultdict(int)
    for i in batallas:
        if regiones == None or i.region in regiones:
            dic_batalla[i.nombre]+=len(i.comandantes_atacantes)
            dic_batalla[i.nombre]+=len(i.comandantes_atacados)
    #dic_batalla = {i.nombre: len(i.comandantes_atacantes) + len(i.comandantes_atacados)\
    #            for i in batallas if regiones == None or i.region in regiones}
    res = sorted(dic_batalla.items(), key = lambda x:x[1], reverse = True)
    if n_batallas!= None:
        res = res[:n_batallas]
    return res

def rey_mas_victorias(batallas:list[BatallaGOT], rol:str="ambos")->str:
    dic_gana = defaultdict(list)
    dic_res = defaultdict(int)
    for i in batallas:
        if i.gana_atacante == True:
            dic_gana[i.rey_atacante].append(1)
        else:
            dic_gana[i.rey_atacado].append(0)
    for c,v in dic_gana.items():
        if rol.lower() == "ambos":
            dic_res[c] = len(v)
        if rol.lower() == "atacante":
            dic_res[c] = sum(v)
        if rol.lower() == "atacado":
            dic_res[c] = len(v) - sum(v)
    return (max(dic_res.items(), key = lambda x:x[1]))

def rey_mas_victorias_por_region(batallas:list[BatallaGOT], rol:str="ambos")->Dict[str, set[str]]:
    dic_regiones = defaultdict(list)
    for i in batallas:
        dic_regiones[i.region].append(i)
    dic_res = {region: rey_mas_victorias(batallas, rol) for region, batallas in dic_regiones.items()}
    for c,v in dic_res.items():
        if v[1] == 0:
            dic_res[c] = None
    return dic_res