# Python proporciona una variedad de métodos para manipular y trabajar con cadenas de caracteres. 
# A continuación se describen los métodos más comunes con ejemplos prácticos de uso en código.

# upper()
# Convierte todos los caracteres de la cadena a mayúsculas.
cadena = "Hola Mundo"
print(cadena.upper()) # HOLA MUNDO

# lower()
# Convierte todos los caracteres de la cadena a minúsculas.
cadena = "Hola Mundo"
print(cadena.lower())   # hola mundo


# capitalize()
# Convierte el primer carácter de la cadena a mayúscula y el resto a minúsculas.
cadena = "hola mundo"
print(cadena.capitalize()) #Hola mundo

# title()
# Convierte el primer carácter de cada palabra a mayúscula y el resto a minúsculas.
cadena = "hola mundo"
print(cadena.title()) #Hola Mundo

# count()
# Cuenta cuántas veces aparece una subcadena en la cadena.
cadena = "Hola mundo, hola universo"
print(cadena.count("hola")) #1

# find()
# Devuelve el índice de la primera aparición de una subcadena en la cadena. Si no se encuentra, devuelve -1.
cadena = "Hola mundo"
print(cadena.find("mundo")) #5

# rfind()
# Devuelve el índice de la última aparición de una subcadena en la cadena. Si no se encuentra, devuelve -1. 
# Comienza a buscar desde la derecha
cadena = "Hola mundo, hola universo"
print(cadena.rfind("hola")) #12

# split()
# Divide la cadena en una lista utilizando el separador especificado.
cadena = "Hola mundo"
print(cadena.split()) #['Hola', 'mundo']

# join()
# Une una lista de cadenas utilizando la cadena como separador.
lista = ["Hola", "mundo"]
print(" ".join(lista)) #Hola mundo

# strip()
# Elimina los caracteres especificados (por defecto, espacios) desde el principio y el final de la cadena.
cadena = "   Hola mundo   "
print(cadena.strip()) #Hola mundo

# replace()
# Reemplaza todas las apariciones de una subcadena por otra subcadena.
cadena = "Hola mundo"
print(cadena.replace("mundo", "universo")) #Hola universo