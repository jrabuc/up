def sumar(a, b):
    return a + b    


def ordenar_arreglo(arreglo):
    for i in range(len(arreglo)):
        for j in range(i + 1, len(arreglo)):
            if arreglo[i] > arreglo[j]:
                arreglo[i], arreglo[j] = arreglo[j], arreglo[i]
    return arreglo
