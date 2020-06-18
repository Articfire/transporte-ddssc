import datetime

def restar_dos_tiempos(tiempo1, tiempo2, fecha1, fecha2):
    fecha_hora_1 = datetime.datetime.combine(fecha1, tiempo1)
    fecha_hora_2 = datetime.datetime.combine(fecha2, tiempo2)
    delta = fecha_hora_2 - fecha_hora_1
    return delta

def calcular_lista_horas(tiempo_inicial, tiempo_final):
    horas = []
    indice = tiempo_inicial.hour

    while indice < tiempo_final.hour:
        horas.append(str(datetime.time(indice, 0)))
        indice += 1
    horas.append(str(tiempo_final))

    return horas
