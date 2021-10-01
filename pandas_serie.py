import numpy as np
import pandas as pd

SEPARADOR = ("x" * 20) + "\n"

#crear una serie con valores iniciales
notas = pd.Series([87, 100, 85, 60, 78])
print(type(notas))
print(notas)
print(SEPARADOR)



#crear una seri de 6 elementos que tengan el mismo valor
iguales = pd.Series(100, range(6))
print(type(iguales))
print(iguales)
print(SEPARADOR)



#estadisticas descriptivas para una serie
print("notas :")
print(f"{notas}")
print(f"cantidad = {notas.count()}")
print(f"media = {notas.mean()}")
print(f"minimo = {notas.min()}")
print(f"maximo = {notas.max()}")
print(f"desviacion standard ={notas.std()}")
print("sumarizacion descriptiva:")
print(notas.describe())
print(SEPARADOR)



#serie con indices personalizados
print("Series con indices personalizados:")
notas_asignadas = pd.Series([87, 100, 85, 60, 78], index=["cresencio", "domitila", "Rutilio", "Panfilo", "Ludoviko"])
print(notas_asignadas)
print(SEPARADOR)

print("Serie generada a partir de un diccionario")
notas_asignadas_dict = pd.Series({"Cresencio":87, "domitila":100, "rutilo":85, "Panfilo":60, "Ludoviko":78})


print(notas_asignadas_dict)
print(SEPARADOR)

#accseso a elementos en una serie con valor de indice 
print(f"la calificacion de rutilo es {notas_asignadas_dict['rutilo']}")
print(f"la calificacion de rutilo es {notas_asignadas_dict.rutilo}")

