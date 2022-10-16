import time

def hora():
    hora =  int(time.strftime('%H'))

    match hora:
        case hora if hora > 19: print("Es Hora de ir a Casa!")
        case hora if hora < 19:
            tiempo_salida = 19
            tiempo_espera = tiempo_salida - hora
            print(f'Faltan {tiempo_espera} horas para ir a casa!')


hora()