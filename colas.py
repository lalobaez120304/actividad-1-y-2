"""
implementacion de colas mediante listas y deque()
demustra la diferencia en la forma de implementacion

"""

#las colas son colecciones de elementos ordenados que unicamente permiten dos acciones:
#añadir un elemento a la cola, sacar un elemento de la cola.

SEPARADOR =("x" * 20) + "\n"
import collections

cola = collections.deque()  #cola utilizando deque

for cantidad in range(5):
    nuevo = input("nombre del recien llegado:")
    cola.appened(nuevo)

print(f"se agregaron {len(cola)}, elementos:")
for elemento in cola:
    print(elemento)
print(SEPARADOR)
pass    #hacer notar que los elementos permanecen en la cola

print("procedamos a retirarlos de la cola")
while cola:
    print(cola.popleft())
pass  #verificar que la estructura se encuentre vacia   
 

