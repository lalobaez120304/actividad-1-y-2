import datetime
SEPARADOR ="x" * 30
#Se desea capturar una lista de fechas de nacimiento (3) y se debera informar cuantos
#años cumple estas personas en el año en curso

lista_fechas  = []
for elemento in range(3) :
    fecha_capturada = input("dime una fecha (dd/mm/aaaa): \n"()
    fecha_procesada = datetime.datetime.strptime(fecha_capturada, "%d/$m/%y").date()
    lista_fechas.append(fecha_procesada)


print(SEPARADOR)

lista_edades = [datetime.date.today().year - fecha.year for fechain lista_fechas]

print(lista_edades)



