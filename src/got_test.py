from got import*

def test_lee_batallas(datos:list[BatallaGOT]):
    print("\ntest_lee_batallas")
    print(f"numero registros leidos: {len(datos)}")
    print(f"\nlos tres primeros: {datos[:3]}")
    print(f"\nlos tres ultimos: {datos[-3:]}")

def test_reyes_mayor_menor_ejercito(datos:list[BatallaGOT]):
    print("\ntest_reyes_mayor_menor_ejercito")
    print(f"los reyes con mayor y menor ejercito respectivamente son: {reyes_mayor_menor_ejercito(datos)}")

def test_batallas_mas_comandantes(datos:list[BatallaGOT]):
    print("\ntest_batallas_mas_comandantes")
    numero = 4
    conjunto_regiones = {'The North', 'The Riverlands'}
    print(batallas_mas_comandantes(datos, conjunto_regiones, numero))

def test_rey_mas_victorias(datos:list[BatallaGOT]):
    print("\ntest_rey_mas_victorias")
    rol = "ambos"
    print(f"El rey con mas victoris es: {rey_mas_victorias(datos, rol)}")
    rol = "atacante"
    print(f"El rey atacante con mas victoris es: {rey_mas_victorias(datos, rol)}")
    rol = "atacado"
    print(f"El rey atacado con mas victoris es: {rey_mas_victorias(datos, rol)}")

def test_rey_mas_victorias_por_region(datos:list[BatallaGOT]):
    print("\ntest_rey_mas_victorias_por_region")
    print("\nReyes con mas victorias por region")
    rol = "ambos"
    for c,v in rey_mas_victorias_por_region(datos, rol).items():
        print(f"{c} --> {v}")
    print("\nReyes atacantes con mas victorias por region")
    rol = "atacante"
    for c,v in rey_mas_victorias_por_region(datos, rol).items():
        print(f"{c} --> {v}")
    print("\nReyes atacados con mas victorias por region")
    rol = "atacado"
    for c,v in rey_mas_victorias_por_region(datos, rol).items():
        print(f"{c} --> {v}")

if __name__=="__main__":
    datos = lee_batallas("data/battles.csv")
    test_lee_batallas(datos)
    test_reyes_mayor_menor_ejercito(datos)
    test_batallas_mas_comandantes(datos)
    test_rey_mas_victorias(datos)
    test_rey_mas_victorias_por_region(datos)