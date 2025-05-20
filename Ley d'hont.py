# Programa simplificado para calcular escaños según la Ley D'Hondt

# Pedir número de escaños
escaños = int(input("Introduce el número de escaños: "))

# Listas para almacenar partidos y votos
partidos = []
votos = []

# Recoger datos de partidos y votos
continuar = True
while continuar:
    partido = input("Introduce el nombre del partido (o 'fin' para terminar): ")
    if partido.lower() == 'fin':
        continuar = False
    else:
        voto = int(input(f"Introduce los votos para el partido {partido}: "))
        partidos.append(partido)
        votos.append(voto)

# Comprobar si hay datos
if len(partidos) == 0:
    print("No se introdujeron partidos.")
elif sum(votos) == 0:
    print("No se introdujeron votos válidos.")
else:
    # Calcular los escaños usando Ley D'Hondt sin NumPy
    escaños_asignados = [0] * len(partidos)
    
    # Crear tabla de divisores
    divisores = []
    for i in range(len(partidos)):
        fila = []
        for j in range(1, escaños + 1):
            fila.append(votos[i] / j)
        divisores.append(fila)
    
    # Asignar escaños
    for _ in range(escaños):
        # Encontrar el mayor valor y su posición
        max_valor = 0
        partido_max = 0
        
        for i in range(len(partidos)):
            for j in range(len(divisores[i])):
                if divisores[i][j] > max_valor:
                    max_valor = divisores[i][j]
                    partido_max = i
                    divisor_max = j
        
        # Asignar escaño y marcar el valor como usado
        escaños_asignados[partido_max] += 1
        divisores[partido_max][divisor_max] = 0
    
    # Mostrar resultados
    print("Asignación de escaños:")
    for i in range(len(partidos)):
        print(f"{partidos[i]}: {escaños_asignados[i]} escaños")

# Este programa calcula cómo se reparten escaños (asientos) en un congreso
# Paso 1: Pedir cuántos escaños hay que repartir en total
# 
# Paso 2: Se crean dos arrays vacíos:
#   - 'partidos': para guardar los nombres de los partidos políticos
#   - 'votos': para guardar cuántos votos recibió cada partido
#
# Paso 3: Recoge los datos de cada partido y sus votos:
#   - Preguntamos por el nombre del partido
#   - Si escribimos un nombre de partido, pregunta cuántos votos obtuvo
#   - Añadimos el partido al array 'partidos' y sus votos a la lista 'votos'
#
# Paso 4: Comprobamos si hay datos para trabajar:
#   - Si no hay partidos, muestra un mensaje y termina
#   - Si todos los votos suman cero, muestra un mensaje y termina
#
# Paso 5: Aplicamos la Ley D'Hondt:
#   - Se crea un array 'escaños_asignados' con ceros para cada partido
#   - Se crea una tabla de 'divisores' donde:
#     Cada fila representa un partido
#     Cada columna representa sus votos divididos por 1, 2, 3, etc.
#   - Por ejemplo, si un partido tiene 1000 votos, su fila será:
#     [1000, 500, 333.33, 250, 200, ...] (votos divididos por 1, 2, 3, 4, 5...)
#
# Paso 6: Asignamos los escaños uno por uno:
#   - Para cada escaño que debemos asignar:
#     Buscamos el valor más alto en toda la tabla de divisores
#     Ese escaño va para el partido que tenga ese valor
#     Marcamos ese valor como usado (poniéndolo a 0)
#     Sumamos 1 escaño al partido ganador en 'escaños_asignados'
#
# Paso 7: Mostramos los resultados:
#   - Para cada partido, imprimimos su nombre y cuántos escaños ha conseguido
#
# La Ley D'Hondt da más escaños a los partidos con más votos, pero de forma proporcional. Al dividir los votos entre 1, 2, 3, etc.,
# estamos simulando lo que pasaría si ya tuvieran 0, 1, 2, etc. escaños.
