"""
ES una lista de pares de elementos con estructura clave:valor
No se accesa a los elementos por posicion, sino por el valor de su clave
La clave puede ser de cualquier tipo imutable (bolean, integer, string, etc.)
Se delimita con {}
A un diccionario se le refiere tambien como dict
"""

#creacion de diccionarios
diccionario_vacio ={}
diccionario_citas ={" ICalla":"wakanda forever",
                      "Thanos":"the hardest choices requiere the strongest wills", 
                      "AMLO":"me canso ganso"}
print(diccionario_citas)
pass

#accesar elementos
print(diccionario_citas["Thanos"])
pass

#agregar elementos:se agrega la nueva llave y se indica su valor
print("x" * 20)
diccionario_citas["plankton"] = "¡por fin tengo la formula de la cangreburger"
print(diccionario_citas)
pass

#eliminar elementos de un diccionario
print("x" * 20)
del diccionario_citas["AMLO"]
print(diccionario_citas)
pass

#opciones para obtener el volcado de un diccionario,
#en cada una, la respuesta debe convertirse a una lista primero
#para un mas facil manejo

#opcion 1 todas las claves, solamente las claves
print(list(diccionario_citas.keys()))
pass

#opcion 2 todos los valores, solamente los valores
print(list(diccionario_citas.values()))
pass

#opcion 3 todos los elementos, elemento por elemento
print(list(diccionario_citas.items()))
