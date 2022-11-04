#Lista con 8 elementos
lista = [1, 2, 3, 4, 5, 6, 7, 8]

# Función que suma el valor de una lista con 8 elementos
def suma_lista(lista):
    suma = 0
    for i in range(8):
        suma += lista[i]
    return suma
print(suma_lista(lista))