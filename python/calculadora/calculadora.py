import operaciones

print("Bienvenido al programa operaciones: \n1) Suma. \n2) Resta. \n3) Multiplicacion. \n4) Division.\n")
valor = int(input("Que operacion quieres realizar?\n"))

match valor:
    case 1: 
        num1 = complex(input("Primer valor:\n"))
        num2 = complex(input("Segundo valor:\n"))
        suma = operaciones.suma(num1.real,num2.real)
    case 2: 
        num1 = complex(input("Primer valor:\n"))
        num2 = complex(input("Segundo valor:\n"))
        suma = operaciones.resta(num1.real,num2.real)
    case 3: 
        num1 = complex(input("Primer valor:\n"))
        num2 = complex(input("Segundo valor:\n"))
        suma = operaciones.multiplicacion(num1.real,num2.real)
    case 4: 
        num1 = complex(input("Primer valor:\n"))
        num2 = complex(input("Segundo valor:\n"))
        suma = operaciones.division(num1.real,num2.real)