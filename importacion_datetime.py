""" ejemplo para ilustrar la importacion de la libreria datetime en python 3 demuestra el uso de : hora, fecha y aritmetica de fecha """

import datetime
import time
SEPARADOR = ("x" * 20) + "\n"

#creacion de una hora especifica
hora = datetime.time(10, 20, 30)
print(f"el tipo de objeto de la hora es {type(hora)}")
print(f"la hora es {hora}")
print(f"la hora de {hora} es {hora.hour}")   #limitado 0..23
print(f"el minuto de {hora} es {hora.minute}")  #limitado 0..59
print(f"el segundo de {hora} es {hora.second}")  # limitado 0..59
print(f"el microsegundo de {hora} es {hora.microsecond}")    #limitado 0.999
print (SEPARADOR * 2)

#determinar la fecha del sistema
fecha_actual = datetime.date.today()
print(f"el tipo de objeto de la fecha es {type(fecha_actual)}")
print(f"la fecha actual es {fecha_actual}")
print(f"el año actual es {fecha_actual.year}")
print(f"el mes actual es {fecha_actual.month}")
print(f"el dia actual es {fecha_actual.day}")
print (SEPARADOR *2)

#convertir a un string a fecha
fecha_capturada = input("dime una fecha (dd/mm/aaaa): \n")
fecha_procesada = datetime.datetime.strptime(fecha_capturada, "%d/%m/%y").date()
print






