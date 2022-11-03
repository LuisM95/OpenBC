cadena = list(set(input("Ingrese los paises: \n").split(", ")))


def odernar_lista(x):
    x.sort()

    for elem in x:
        print(elem)

odernar_lista(cadena)