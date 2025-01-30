# Métodos de Listas en Python

# Python proporciona varios métodos para manipular y modificar listas de manera eficiente. 
# A continuación se explican algunos de los métodos más comunes junto con ejemplos prácticos de uso en código.

# clear()
# El método clear() elimina todos los elementos de una lista, dejándola vacía.
letras = ['a', 'b', 'c', 'd', 'e']
letras.clear()
print(letras) # []

# extend()
# El método extend() añade todos los elementos de un iterable (lista, tupla, etc.) al final de la lista actual.
numeros = [1, 2, 3]
numeros.extend([4, 5, 6])
print(numeros) # [1, 2, 3, 4, 5, 6]

# insert()
# El método insert() inserta un elemento en una posición específica de la lista. 
# El primer argumento es el índice en el que se insertará el elemento y el segundo argumento es el elemento a insertar.
numeros = [1, 2, 3, 4]
numeros.insert(2, 'a')
print(numeros) #[1, 2, 'a', 3, 4]

# reverse()
# El método reverse() invierte el orden de los elementos en la lista.
numeros = [1, 2, 3, 4, 5]
numeros.reverse()
print(numeros) # [5, 4, 3, 2, 1]

# sort()
# El método sort() ordena los elementos de la lista en orden ascendente por defecto. 
# Se puede usar el argumento reverse=True para ordenar en orden descendente.
numeros = [5, 2, 9, 1, 5, 6]
numeros.sort()
print(numeros) #[1, 2, 5, 5, 6, 9]

numeros = [5, 2, 9, 1, 5, 6]
numeros.sort(reverse=True) #al reves
print(numeros) # [9, 6, 5, 5, 2, 1]