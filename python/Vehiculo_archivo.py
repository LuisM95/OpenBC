class Vehiculo():
    color = None
    puertas = None
    ruedas = None
    cilindrada = None
    velocidad = None

    def __init__(self, color, puertas, ruedas, cilindrada, velocidad):
        self.color = color
        self.puertas = puertas
        self.ruedas = ruedas
        self.cilindrada = cilindrada 
        self.velocidad = velocidad 

    def __repr__(self):
        return f'Detalles carro:\n color: {self.color} \n Puertas: {self.puertas} \n Ruedas: {self.ruedas} \n Cilindrada: {self.cilindrada} \n Velocidad: {self.velocidad}'

v1 = Vehiculo('Gray', 5, 4, 140, 240)

def escribe(fichero,):
    f = open(fichero, 'w')
    f.write(str(v1.__repr__()))
    f.close()

escribe('python/Vehiculo.txt')
