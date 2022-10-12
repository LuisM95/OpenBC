class Alumno:
    nombre = None
    nota1 = None
    nota2 = None

    def __init__(self,nombre,nota1,nota2):
        self.nombre = nombre
        self.nota1 = nota1
        self.nota2 = nota2
        self.resultado = (nota1 + nota2)/2

        if self.resultado >= 6:
            print(f'Felicidades {self.nombre} Has aprobado el curso con un promedio de {self.resultado}')

        elif self.resultado < 6:
            print(f'Lo sentimos {self.nombre} No has aprobado el curso, y tu promedio es {self.resultado}')


a1 = Alumno("Eduardo",7,9)
a2 = Alumno("Gaia", 4, 6)