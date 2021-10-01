import numpy as np
SEPARADOR = ("X" * 20) + "\n"

a = np.array([[2,0],[3,0],[3,1],[5,0],[5,1],[5,2]])
print(a)
print(type(a))
print(SEPARADOR)

a[:,0] = 15
print(a)
print(SEPARADOR)

a[:,1] = 30
print(a)
print(SEPARADOR)

#inicializacion de arreglos
print("arreglo2: 2 renglones, 4 columnas")
arreglo2 = np.zeros(shape=(2,4), dtype= int)
print(arreglo2)
print(arreglo2.shape)
print(SEPARADOR)

dos_en_dos = np.arange(10,25,2) #cifras separadas de dos en dos 
print(dos_en_dos)
print(dos_en_dos.shape)
pass


