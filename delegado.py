import numpy as np    
candidatos = np.empty(5, dtype=object)

candidatos[0] = input("Introduce el nombre del candidato 1: ")
candidatos[1] = input("Introduce el nombre del candidato 2: ")
candidatos[2] = input("Introduce el nombre del candidato 3: ")
candidatos[3] = input("Introduce el nombre del candidato 4: ")
candidatos[4] = input("Introduce el nombre del candidato 5: ")

votos = np.zeros(5, dtype=int)

votos[0] = int(input("Introduce el número de votos del candidato 1: "))  
votos[1] = int(input("Introduce el número de votos del candidato 2: "))
votos[2] = int(input("Introduce el número de votos del candidato 3: "))
votos[3] = int(input("Introduce el número de votos del candidato 4: "))
votos[4] = int(input("Introduce el número de votos del candidato 5: "))

print("Los votos son:", votos)
print("Los candidatos son:", candidatos)
print("El candidato 1 tiene", votos[0], "votos.")
print("El candidato 2 tiene", votos[1], "votos.")
print("El candidato 3 tiene", votos[2], "votos.")
print("El candidato 4 tiene", votos[3], "votos.")
print("El candidato 5 tiene", votos[4], "votos.")

if votos[0] > votos[1] and votos[0] > votos[2] and votos[0] > votos[3] and votos[0] > votos[4]:
    print("El candidato 1 ha ganado.")
elif votos[1] > votos[0] and votos[1] > votos[2] and votos[1] > votos[3] and votos[1] > votos[4]:
    print("El candidato 2 ha ganado.")
elif votos[2] > votos[0] and votos[2] > votos[1] and votos[2] > votos[3] and votos[2] > votos[4]:
    print("El candidato 3 ha ganado.")
elif votos[3] > votos[0] and votos[3] > votos[1] and votos[3] > votos[2] and votos[3] > votos[4]:
    print("El candidato 4 ha ganado.")
elif votos[4] > votos[0] and votos[4] > votos[1] and votos[4] > votos[2] and votos[4] > votos[3]:
    print("El candidato 5 ha ganado.")
else:
    print("Ha habido un empate.")
