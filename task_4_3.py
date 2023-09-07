'''
Gandarilla Carrillo Fernando Christian
08/21/2023

Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido. NOTA: No usar ciclos.

Ejemplo

Entrada:
    Nombre: Pedro
    Número: 5

Salida:
   Pedro
   Pedro
   Pedro
   Pedro
   Pedro
'''

# Get values
name = input("Inserta nombre: ")
times = int(input("Inserta numero de veces a repetir: "))

# Create string
result = (name + '\n') * times

# Print results
print(result)