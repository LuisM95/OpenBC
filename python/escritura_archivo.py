
def escribe(fichero, datos):
    f = open(fichero, 'w')

    for linea in datos:
        if linea.endswith('\n') == False:
        	linea = linea + '\n'
        
        
        f.write(linea)

    f.close()

lista =[
    'Escribiendo un fichero con python', 
    'con El curso de openbootcamp', 
    'desde codespaces'
]

escribe('miarchivo.txt', lista)