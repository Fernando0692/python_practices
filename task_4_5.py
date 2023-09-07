'''
Gandarilla Carrillo Fernando Christian
08/21/2023

Escribir un programa que pregunte el nombre del usuario en la consola para obtener como salida lo siguiente:
<NOMBRE> tiene <n> letras, (donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de letras que tienen el nombre)
Imprimir la cantidad de vocales y consonantes que tiene el nombre.
'''

# Get full name
name = input("Ingresa tu nombre: ")

upperName = name.upper()
lengthName = len(name)

def getTotals(nombre):
    vocals = "AEIOUaeiou"
    numVocals = sum(1 for letter in name if letter in vocals)
    numConso = len(nombre) - numVocals
    return numVocals, numConso

numVocals, numConso = getTotals(name)

# Print results
print(upperName, " tiene ",lengthName, " letras.")
print("Cantidad de vocales:", numVocals)
print("Cantidad de consonantes:", numConso)