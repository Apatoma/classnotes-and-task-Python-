import numpy as np

def ley_dhont(cuentavotos, num_escaños):
    """
    Aplica la Ley d'Hondt para asignar escaños a partidos políticos.

    :param cuentavotos: Lista con los votos obtenidos por cada partido.
    :param num_escaños: Número total de escaños a repartir.
    :return: Lista con los escaños asignados a cada partido.
    """
    # Declarar una matriz para calcular los restos de votos
    escanos = np.zeros((len(cuentavotos), num_escaños))

    # Calcular los restos de votos
    for i in range(len(cuentavotos)):
        for j in range(1, num_escaños + 1):  # Divisiones desde 1 hasta num_escaños
            escanos[i][j - 1] = cuentavotos[i] / j

    # Asignar escaños
    asignados = [0] * len(cuentavotos)  # Lista para contar los escaños asignados
    for _ in range(num_escaños):
        # Buscar el valor máximo en la matriz de restos
        max_index = np.unravel_index(np.argmax(escanos, axis=None), escanos.shape)
        partido = max_index[0]  # Índice del partido con el mayor resto
        asignados[partido] += 1  # Asignar un escaño al partido
        escanos[partido, max_index[1]] = -1  # Marcar el resto como usado

    return asignados

# Ejemplo de uso
if __name__ == "__main__":
    # Ejemplo de votos por partido
    cuentavotos = [340000, 280000, 160000]  # Votos obtenidos por cada partido
    num_escaños = 10  # Número total de escaños a repartir

    # Calcular la asignación de escaños
    asignación = ley_dhont(cuentavotos, num_escaños)

    # Mostrar resultados
    print("Votos por partido:", cuentavotos)
    print("Número de escaños asignados:", asignación)
