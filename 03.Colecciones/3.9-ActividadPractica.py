# Colecciones> Consigna

# A partir de una lista realizar las siguientes tareas sin modificar la lista original:
# Borrar los elementos duplicados
# Ordenar la lista de mayor a menor
# Eliminar todos los números impares ( for ---- if (%2==1) ---- pop, remove )
# Realizar una suma de todos los números que quedan (sum(lista))
# Añadir como primer elemento de la lista la suma realizada insert(0, suma)
# Devolver la lista modificada
# Finalmente, después de ejecutar la función, comprueba que la suma de todos los números a partir del segundo, concuerda con el primer número de la lista
# lista = [29, -5, -12, 17, 5, 24, 5, 12, 23, 16, 12, 5, -12, 17]
# Nota: Recuerda que para sumar todos los números de una lista puedes usar sum


lista = [29, -5, -12, 17, 5, 24, 5, 12, 23, 16, 12, 5, -12, 17]

# Borrar los elementos duplicados
lista_sin_duplicados = list(set(lista))
print(lista_sin_duplicados)

# Ordenar la lista de mayor a menor
lista_sin_duplicados.sort(reverse=True)
print(lista_sin_duplicados)

# Eliminar todos los números impares
lista_sin_impares  = list(set(lista))
for numeros in lista_sin_impares[:]:
    if numeros %2 == 1:
        lista_sin_impares.remove(numeros)
lista_sin_impares.sort()
print(lista_sin_impares)

# Realizar una suma de todos los números que quedan (sum(lista))
total_impares = sum(lista_sin_impares)
print(total_impares)

# Añadir como primer elemento de la lista la suma realizada insert(0, suma)
lista_sin_impares.insert(0, total_impares)
print(lista_sin_impares)