peso = -1
while peso != 0:
    peso = float(input("Introduce tu peso en kg (o 0 para salir): "))
    
    # Si el peso es 0, salir del bucle
    if peso == 0:
        print("Programa terminado.")
        break
        
    # Pedir resto de datos solo si no se quiere salir
    altura = float(input("Introduce tu altura en metros (usa puntos en vez de comas): "))
    edad = int(input("Introduce tu edad en años: "))

    if peso <= 0 or altura <= 0 or edad <= 0:
        print("Por favor, introduce valores válidos para peso, altura y edad.")
        continue  # Volver al inicio del bucle

    imc = peso / (altura ** 2)  # Fórmula del IMC
    print("Tu IMC es:", round(imc, 2))

    if imc < 22 and edad < 45:
        print("Tu IMC es bajo para tu edad.")
    elif imc < 22 and edad >= 45:
        print("Tu IMC es medio para tu edad.")
    elif imc >= 22 and edad < 45:
        print("Tu IMC es medio para tu edad.")  