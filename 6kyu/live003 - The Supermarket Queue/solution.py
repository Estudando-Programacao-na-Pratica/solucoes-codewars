"""
Doctests:
>>> queue_time([5,3,4], 1)
12
>>> queue_time([10,2,3,3], 2)
10
>>> queue_time([2,3,10], 2)
12
"""


def queue_time(customers, n):
    if len(customers) == 0:
        return 0

    if n > len(customers):
        return max(customers)

    fila = []
    tempo = 0
    contador = n

    for i in range(n):
        fila.append(customers[i])

    while contador < len(customers):
        minimo = min(fila)

        for i in range(n):
            fila[i] = fila[i] - minimo
        tempo += minimo

        for i in range(n):
            if fila[i] == 0:
                fila[i] = customers[contador]
                contador += 1
    tempo += max(fila)
    return tempo
