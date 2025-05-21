import numpy as np    
candidatos = []
votos = []
nombre = -1

while nombre != "":
    nombre = input("Introduce el nombre del candidato o pulsa ENTER para terminar: ")
    if nombre != "":  
        candidatos.append(nombre)

for candidato in candidatos:
    voto = int(input(f"Introduce el número de votos de {candidato}: "))
    votos.append(voto)

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