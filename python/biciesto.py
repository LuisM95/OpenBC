def bisiesto(n):
    if  n % 4 != 0:
        print("El año {} no es bisiesto:".format(n))
    elif n % 4 == 0 and n % 100 !=0:
        print("El año {} es bisiesto".format(n))
    elif n % 4 == 0 and n % 100 == 0 and n % 400 != 0:
        print("El año {} no es bisiesto".format(n))
    elif n % 4 == 0 and n % 100 == 0 and n % 400 == 0:
        print("El año {} es bisiesto".format(n))
 
n = int(input("Ingresa el año: \n"))
bisiesto(n)