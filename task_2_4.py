'''
Gandarilla Carrillo Fernando Christian
08/21/2023
Actividad 2.4 Escribir el codigo que permita resolver lo siguiente: Leer dos números, calcular suma, resta, multiplicación y división. Imprimir resultado con el siguiente formato:
*** Resultados ***
2 + 2 = 4
2 - 2 = 0
2 * 2 = 4
2 / 2 = 1

Tambien se solicita imprimir los mensajes correspondientes,
'''
# Convert values
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))

# Operations
sum = a + b
subs = a - b
multiplicacion = a * b
division = a / b

# Print results
print("*** Resultados ***")
print(f"{a} + {b} = {sum}")
print(f"{a} - {b} = {subs}")
print(f"{a} * {b} = {multiplicacion}")
print(f"{a} / {b} = {division}")