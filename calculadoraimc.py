# Calculadora de Índice de Masa Corporal (IMC)

while True:
    print("Calculadora de IMC")
    peso = float(input("Introduce tu peso en kg (o 0 para salir): "))
    if peso == 0:
        print("Programa finalizado.")
        break
    altura = float(input("Introduce tu altura en metros (usa puntos en vez de comas): "))
    edad = int(input("Introduce tu edad en años: "))

    if peso <= 0 or altura <= 0 or edad <= 0:
        print("Por favor, introduce valores válidos para peso, altura y edad.")

    imc = peso / (altura ** 2)  # Fórmula del IMC
    print("Tu IMC es:", imc)

    if imc < 22 and edad < 45:
        print("Tu IMC es bajo para tu edad.")
    if imc < 22 and edad >= 45:
        print("Tu IMC es medio para tu edad.")
    if imc >= 22 and edad < 45:
        print("Tu IMC es medio para tu edad.")
    else:
        print("Tu IMC es alto para tu edad.")
