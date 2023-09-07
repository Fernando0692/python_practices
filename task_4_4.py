'''
Gandarilla Carrillo Fernando Christian
08/21/2023

Escribir un programa que pregunte en la consola el nombre completo del usuario y después muestre por pantalla el nombre completo del usuario como se indica a continuación:
En letras minúsculas
En letras mayúsculas
Letra inicial en mayúscula del nombre y apellido
Importante: El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.
'''

# Get full name
fullName = input("Ingresa tu nombre completo: ")

# Lowe name
lowerName = fullName.lower()
print("En letras minúsculas: ", lowerName)

# Upper name
upperName = fullName.upper()
print("En letras mayúsculas: ", upperName)

# Capital for name and lastname
capital = " ".join([name.capitalize() for name in fullName.split()])
print("Letra inicial en mayúscula del nombre y apellido:", capital)
