'''
Gandarilla Carrillo Fernando Christian
08/20/2023
Actividad 2.3 Escribir el codigo que permita resolver lo siguiente: Una panadería vende las barras de pan a $20. El pan que no es del día tiene un descuento del 30%. Se pide escribir un programa que lea el número de barras vendidas que no son del día. Mostrar el precio habitual, el descuento y el coste final, tambien se solicita imprimir los mensajes correspondientes; deberá incluir  comentarios necesarios para documentar el codigo y su nombre.
'''

def breadPrices(x):
    total = x * 20
    priceDescount = total * 0.30
    finalTotal = total - priceDescount
    
    print(f"Subtotal: ${total}")
    print(f"Descuento: ${priceDescount}")
    print(f"total: ${finalTotal}")

breadsInput = input("Ingrese el número de barras de pan: ")

try:
    number = int(breadsInput)
    if number >= 0:
        breadPrices(number)
    else:
        print("La cantidad debe ser un valor entero.")
except ValueError:
    print("Ingrese un valor válido.")
