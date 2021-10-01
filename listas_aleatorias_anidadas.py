import random
SEPARADOR= ("X" * 20) +"\n"

#creacion de una lista con diez valores aleatorios entre el 1 y el 100
lista = [random.randrange(1,101) for valor in range(10)]
print(type(lista))
print(f"el primer elemento es {lista[0]} y el ultimo es {lista(9)}")
print(type(lista))
print(SEPARADOR)

#creacion  de una lista de cinco listas con diez elementos cada una 
lista_de_listas = [[random.randrange(1,101) for valor in range(10)] for valor in range(5)]
print(lista_de_listas)
print(f"el primer elemento es {lista_de_listas[0][0]} y el ultimo es {lista_de_listas[4][9]}>")
#print(lista_de_listas[0][:])
print(lista_de_listas[0])
for lista_interna in lista_de_listas:
    print(lista_interna[0])

print(type(lista_de_listas))

print("[")
for lista_de_primer_nivel in lista_de_listas:
    #print(f"lista interna: {lista_primer_nivel}")
    print("[", end="")
    for elemento in lista_primer_nivel:
        print(f"{elemento}",end="\t")
    print("]", end="")
    print("")
print("]")
print(SEPARADOR)

print(f"el elemento 8,2 es{lista-de-listas[8][2]}")
print(f"el elemento 2,7 es {lista_de_listas[2][7]}")