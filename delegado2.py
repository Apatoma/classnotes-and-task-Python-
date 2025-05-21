#en esta version del programa del delegado, se ha añadido la funcion de que el usuario añada los votos uno por uno, sumandolos al candidato.
import numpy as np    
candidatos = []
nombre = -1

while nombre != "":
    nombre = input("Introduce el nombre del candidato o pulsa ENTER para terminar: ")
    if nombre != "":  
        candidatos.append(nombre)

# Inicializa los votos en 0 para cada candidato
votos = [0] * len(candidatos)

print("Introduce los votos uno a uno. Escribe ENTER para terminar.")
while True:
    voto = input("¿A qué candidato le das el voto? (nombre o ENTER para terminar): ")
    if voto == "":
        break
    if voto in candidatos:
        idx = candidatos.index(voto)
        votos[idx] += 1
    else:
        print("Candidato no válido. Intenta de nuevo.")

print("Los votos son:", votos)
print("Los candidatos son:", candidatos)

mayor_votos = 0
ganadores = []

for i in range(len(candidatos)):
    if votos[i] > mayor_votos:
        mayor_votos = votos[i]
        ganadores = [candidatos[i]]
    elif votos[i] == mayor_votos:
        ganadores.append(candidatos[i])

if len(ganadores) == 1:
    print("El ganador es", ganadores[0], "con", mayor_votos, "votos.")
else:
    print("Hay un empate entre:", ", ".join(ganadores), "con", mayor_votos, "votos.")