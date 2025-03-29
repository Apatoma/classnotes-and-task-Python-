while True:
    tipo = int(input("Introduce 1 para sumar, 2 para restar, 3 para multiplicar, 4 para dividir, o 0 para salir: "))

    if tipo == 0:
        print("Saliendo del programa.")
        break

    if tipo == 1:
        print("Suma")
        a = int(input("Introduce el primer número: "))
        b = int(input("Introduce el segundo número: "))
        resultado = a + b
        print("el resultado es:", resultado)

    elif tipo == 2:
        print("Resta")
        a = int(input("Introduce el primer número: "))
        b = int(input("Introduce el segundo número: "))
        resultado = a - b
        print("el resultado es:", resultado)

    elif tipo == 3:
        print("Multiplicación")
        a = int(input("Introduce el primer número: "))
        b = int(input("Introduce el segundo número: "))
        resultado = a * b
        print("el resultado es:", resultado)

    elif tipo == 4:
        print("División")
        a = int(input("Introduce el primer número: "))
        b = int(input("Introduce el segundo número: "))
        if b == 0:
            print("No se puede dividir entre cero.")
        else:
            resultado = a / b
        print("el resultado es:", resultado)

    else:
        print("Tipo de operación no válida")