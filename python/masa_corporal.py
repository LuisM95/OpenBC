masa = float(input("Ingresa tu masa corporal en KG: \n"))
estatura = float(input("Ingresa tu Estatura en Metros: \n"))

masa_corporal = masa / estatura ** 2

print("Tu Masa Corporal es: {:.2f}".format(masa_corporal))