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
ganador = ""

for i in range(len(candidatos)):
    if votos[i] > mayor_votos:
        mayor_votos = votos[i]
        ganador = candidatos[i]

print("El ganador es", ganador, "con", mayor_votos, "votos.")