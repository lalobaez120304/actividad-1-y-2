

import random
SEPARADOR = ("x" * 20) + "\n"

print (f"obteniendo un numero entero aleatorio que puede ir del 0 al 19: {random.randrange(20)}")
print (SEPARADOR)
print (f"obteniendo un numero entero aleatorio par que puede ir del 2 al 20: {random.randrange(2, 21, 2)}")
print (SEPARADOR)
print (f"obteniendo un valor numerico entre 0.0 y 1.0: {random.random()}")
print (SEPARADOR * 2)

listaDePrueba = [10, 20, 30, 40, 15, 25, 35, 45]
print (f"la lista de prueba es {listaDePrueba}")
print (f"El valor seleecionado aleatoriamente de la lista anterior es {random.choice(listaDePrueba)}")
print (SEPARADOR)
random.shuffle(listaDePrueba)
"la funcion random. shuffle devuelve la secuencia x pasada como argumento desordenada."
print (f"la lista ya 'perturbada/barajada' es {listaDePrueba}")
