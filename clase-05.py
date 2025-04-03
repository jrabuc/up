def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b

def dividir(a, b):  
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b

def potencia(a, b): 
    return a ** b

def raiz(a):
    if a < 0:
        raise ValueError("No se puede calcular la raíz cuadrada de un número negativo")
    
def factorial(n):   
    if n < 0:
        raise ValueError("No se puede calcular el factorial de un número negativo")
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)