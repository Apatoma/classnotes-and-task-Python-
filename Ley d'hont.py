import numpy as np

partidos = []
votos = []
escaños = int(input("Introduce el número de escaños: "))
while True:
    partido = input("Introduce el nombre del partido (o 'fin' para terminar): ")
    if partido.lower() == 'fin':
        break
    else:
        votos_partido = input(f"Introduce los votos para el partido {partido}: ")
        partidos.append(partido)
        votos.append(int(votos_partido))

if len(partidos) == 0:
    print("No se introdujeron partidos.")
elif votos_partido == 0:
    print("No se introdujeron votos.")

# Ley D'Hondt
def ley_dhondt(votos, escaños):
    cocientes = np.zeros((len(votos), escaños))
    for i in range(len(votos)):
        for j in range(escaños):
            if j == 0:
                cocientes[i][j] = votos[i]
            else:
                cocientes[i][j] = votos[i] / (j + 1)
    return cocientes

def asignar_escanos(cocientes, escaños):
    asignacion = np.zeros(len(cocientes))
    for i in range(escaños):
        max_index = np.unravel_index(np.argmax(cocientes), cocientes.shape)
        asignacion[max_index[0]] += 1
        cocientes[max_index[0]][max_index[1]] = 0
    return asignacion
cocientes = ley_dhondt(votos, escaños)
asignacion = asignar_escanos(cocientes, escaños)
print("Asignación de escaños:")
for i in range(len(partidos)):
    print(f"{partidos[i]}: {asignacion[i]} escaños")
