
def escribe(fichero, datos):
    f = open(fichero, 'w')

    for linea in datos:
        if not linea.endswith('\n'):
            linea = linea + '\n'
        f.write(linea)

    f.close()


lista = [
    'aprendiendo a escribir',
    'un archivo en python con',
    'openbootcamp y codespaces'
]

escribe('python/miarchivo.txt', lista)

texto = input("Ingresa el texto a agregar:\n")
def agregarTexto( fichero, datos):
    f = open(fichero, 'a')
    if texto != '':
        f.write(texto)
    else:
        print("No hay nada que agregar")

agregarTexto('python/miarchivo.txt', texto)
