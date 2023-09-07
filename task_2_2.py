'''
Gandarilla Carrillo Fernando Christian
08/18/2023
Actividad 2.2 Escribir el codigo que permita Convertir una cantidad N a monedas. Usar monedas de $20, $10, $5, $1. Importante considerar que la cantidad es un valor entero. Tambien se solicita imprimir los mensajes correspondientes. Deberá incluir  incluir  comentarios necesarios para documentar el codigo y su nombre.
'''

def changeCoin(x):
    # Coins of $20
    coins20 = x // 20
    x = x % 20
    
    # Coins of $10
    coins10 = x // 10
    x = x % 10
    
    # Coins of $5
    coins5 = x // 5
    x = x % 5
    
    # Coins of $1
    coins1 = x
    
    # Imprime los resultados
    print(f"Monedas de $20: {coins20}")
    print(f"Monedas de $10: {coins10}")
    print(f"Monedas de $5: {coins5}")
    print(f"Monedas de $1: {coins1}")

# Insert number
numberInput = input("Ingrese cantidad en un numero entero: ")

try:
    number = int(numberInput)
    if number >= 0:
        changeCoin(number)
    else:
        print("La cantidad debe ser un valor entero no negativo.")
except ValueError:
    print("Ingrese un valor entero válido.")
