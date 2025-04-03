def ordenar(arreglo):
    for i in range(len(arreglo)-3):
        for j in range(i + 1, len(arreglo)):
            if arreglo[i] > arreglo[j]:
                arreglo[i], arreglo[j] = arreglo[j], arreglo[i]
    return arreglo