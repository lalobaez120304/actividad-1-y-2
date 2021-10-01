import math
SEPARADOR = ("x" * 20) + "\n"
 
valorFlotante = float(input("introduceun valor con fraccion decimal:\n"))
print(f"El siguiente entero hacia arriba de {valorFlotante} es {math.ceil(valorFlotante)}")
print(SEPARADOR)
print(f"el siguiente entero hacia abajo de {valorFlotante} es {math.floor(valorFlotante)}")
print(SEPARADOR)
print(f"la parte entera truncada de {valorFlotante} es{math.trunc(valorFlotante)} ") #equivalente a floor() para positivos y a ceil() para negativos
print(SEPARADOR * 2)
pass


valorNumerico = int(input("Dame un valor entero:\n"))
print(f"la raiz cuadrada de {valorNumerico} es igual a {math.sqrt(valorNumerico)}")
print(SEPARADOR)
print(f"El factorial de {valorNumerico} es igual a {math.factorial(valorNumerico)} ")
potencia = int(input("dameun valor entero:\n"))
print(f"El resultado de elevar {valorNumerico} a la {potencia} potencia es igual a {math.pow(valorNumerico,potencia)} ")
print(SEPARADOR * 2)
pass


print (f"El valor de Pi es{math.pi}" )
