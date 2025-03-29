import math
import cmath  # Para manejar números complejos

a = float(input("Introduce coeficiente A: "))
b = float(input("Introduce coeficiente B: "))
c = float(input("Introduce coeficiente C: "))

if a == 0:
    # Ecuación lineal
    if b != 0:
        x = -c / b
        print("Ecuación lineal: x =", x)
    else:
        print("No es una ecuación válida.")
else:
    discriminante = b**2 - 4*a*c
    if discriminante >= 0:
        X1 = (-b + math.sqrt(discriminante)) / (2*a)
        X2 = (-b - math.sqrt(discriminante)) / (2*a)
    else:
        # Usar cmath.sqrt para obtener raíces complejas
        X1 = (-b + cmath.sqrt(discriminante)) / (2*a)
        X2 = (-b - cmath.sqrt(discriminante)) / (2*a)
    print("X1 =", X1)
    print("X2 =", X2)

#este programa sirve para calcular las raices cuadradas de una ecuacion de segundo grado, es decir, una ecuacion de la forma ax^2 + bx + c = 0.
#Para ello, se le piden al usuario los coeficientes a, b y c, y se calcula el discriminante.

#A:1, B:2, C:1 ¿qué resultado da?: x1 = -1.0, x2 = -1.0
#A:1, B:-2, C:1 ¿qué resultado da?: x1 = 1.0, x2 = 1.0
#A:0, B:4, C:1 ¿qué resultado da?: x1 = -0.25, x2 = -0.25