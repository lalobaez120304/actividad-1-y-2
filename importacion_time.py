
import time
SEPARADOR = ("x" * 20) + "\n"

segundos = int(input("cantidad de segundos a esperar"))
time.sleep(segundos)
print(f"han transcurrido, por lo menos, {segundos} segundos")
print (SEPARADOR * 2)

print("Iniciaremos la medicion de un proceso simulado")

horaInicial = time.time()

for termino in range(10):
    time.sleep(segundos)

print("proceso simulado concluido")
duracion = time.time() - horaInicial
print(f"la duracion de proceso simulado fue de {duracion} segundos")




