
from tkinter.messagebox import NO
from turtle import color


class Vehiculo():
    color = None
    ruedas = None
    puertas = None

    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas


class Coche(Vehiculo):
        velocidad = None
        cilindrada = None
        
        def __init__(self,velocidad, cilindrada):
            self.velocidad = velocidad
            self.cilindrada = cilindrada

v1 = Vehiculo("Gris", 4, 2)

print("El Vehiculo es color {} \n"
        "Cuenta con {} ruedas \n"
        "Y Tiene {} puertas".format(v1.color, v1.ruedas, v1.puertas))

c1 = Coche(270, 320)

print("El Vehiculo alcanza una velocidad maxima de {} KM/H \n"
        "Y Cuenta con una cilindrada de {} CV".format(c1.velocidad, c1.cilindrada))