from functools import reduce

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15]

def filtro(x):
    if x % 2 != 0:
        return True

    return False

def sumar(a,b):
    return a + b


listaresultado = filter(filtro, numeros)
resultado = reduce(sumar, listaresultado)
print(resultado)