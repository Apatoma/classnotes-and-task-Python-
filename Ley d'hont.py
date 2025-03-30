import numpy as np

partidos = []
votos = []

while True:
    partido = input("Introduce el nombre del partido (o 'fin' para terminar): ")
    if partido.lower() == 'fin':
        break

