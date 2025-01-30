# Métodos de Diccionarios
# Los diccionarios en Python son colecciones de pares clave-valor que permiten almacenar datos de manera eficiente. 
# A continuación se explican algunos de los métodos más comunes para trabajar con diccionarios junto con ejemplos prácticos de uso en código.


# get()
# El método get() devuelve el valor de la clave especificada. Si la clave no se encuentra en el diccionario, devuelve un valor por defecto (opcional).

colores = {
    "amarillo": "yellow", 
    "azul": "blue", 
    "verde": "green"
    }
print(colores.get("amarillo")) # yellow
print(colores.get("rojo", "no hay clave rojo")) # no hay clave rojo


# keys()
# El método keys() devuelve una vista de todas las claves en el diccionario.
colores = {
    "amarillo": "yellow", 
    "azul": "blue", 
    "verde": "green"
    }
print(colores.keys()) #dict_keys(['amarillo', 'azul', 'verde'])


# values()
# El método values() devuelve una vista de todos los valores en el diccionario.
colores = {
    "amarillo": "yellow", 
    "azul": "blue", 
    "verde": "green"
    }
print(colores.values()) #dict_values(['yellow', 'blue', 'green'])


# items()
# El método items() devuelve una vista de todos los pares clave-valor en el diccionario como tuplas.
colores = {
    "amarillo": "yellow", 
    "azul": "blue", 
    "verde": "green"
    }
print(colores.items())  # dict_items([('amarillo', 'yellow'), ('azul', 'blue'), ('verde', 'green')])

colores = {
    "amarillo": "yellow", 
    "azul": "blue", 
    "verde": "green" 
    }
for clave, valor in colores.items():
    print(f"La clave es {clave} y el valor es {valor}") 
    # La clave es amarillo y el valor es yellow
    # La clave es azul y el valor es blue
    # La clave es verde y el valor es green