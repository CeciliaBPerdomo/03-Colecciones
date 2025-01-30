# Métodos de Conjuntos
# Los conjuntos en Python son colecciones desordenadas de elementos únicos. 
# Python proporciona varios métodos para manipular y trabajar con conjuntos. 
# A continuación se describen algunos de los métodos más comunes junto con ejemplos prácticos de uso.

# copy()
# El método copy() devuelve una copia superficial del conjunto.
set1 = {1, 2, 3}
set2 = set1.copy()
print(set2) # {1, 2, 3}

# isdisjoint()
# El método isdisjoint() devuelve True si dos conjuntos no tienen elementos en común.
set1 = {1, 2, 3}
set2 = {4, 5, 6}
print(set1.isdisjoint(set2)) # True

# issubset()
# El método issubset() devuelve True si todos los elementos del conjunto están en otro conjunto.
set1 = {1, 2}
set2 = {1, 2, 3, 4}
print(set1.issubset(set2)) # True

# issuperset()
# El método issuperset() devuelve True si el conjunto contiene todos los elementos de otro conjunto.
set1 = {1, 2, 3, 4}
set2 = {1, 2}
print(set1.issuperset(set2)) # True


# union()
# El método union() devuelve un nuevo conjunto con todos los elementos de los conjuntos originales.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.union(set2)) #{1, 2, 3, 4, 5}

# difference()
# El método difference() devuelve un nuevo conjunto con los elementos que están en el conjunto original pero no en el otro conjunto.
set1 = {1, 2, 3}
set2 = {2, 3, 4}
print(set1.difference(set2)) #1


# difference_update()
# El método difference_update() elimina del conjunto original todos los elementos que están en otro conjunto.
set1 = {1, 2, 3}
set2 = {2, 3, 4}
set1.difference_update(set2)
print(set1) # {1}


# intersection()
# El método intersection() devuelve un nuevo conjunto con los elementos comunes a ambos conjuntos.
set1 = {1, 2, 3}
set2 = {2, 3, 4}
print(set1.intersection(set2)) #{2, 3}

# intersection_update()
# El método intersection_update() actualiza el conjunto original conservando solo los elementos comunes a ambos conjuntos.
set1 = {1, 2, 3}
set2 = {2, 3, 4}
set1.intersection_update(set2)
print(set1) # {2, 3}