'''
Gandarilla Carrillo Fernando Christian
08/21/2023
Escribir un programa que pregunte al usuario una cantidad a invertir, el interes porcentual anual y el número de años. Muestre el capital obtenido de la inversión cada año que dura la inversión.
Ejemplo:

Entrada:
¿Cantidad a invertir? 1000 
¿Interés porcentual anual? 10 
¿Años? 5

Salida:
Capital tras 1 años: 1100.0 
Capital tras 2 años: 1210.0 
Capital tras 3 años: 1331.0 
Capital tras 4 años: 1464.1 
Capital tras 5 años: 1610.51
'''

# Get values for investment amount, annual interest && investment years
amount = float(input("¿Cantidad a invertir? "))
interest = float(input("¿Interés porcentual anual? "))
years = int(input("¿Años? "))

yearCapital = []  # Array for capital

for _ in range(years):
    capital = amount * (1 + (interest / 100))
    yearCapital.append(capital)
    amount = capital

# Print results
for i, capital in enumerate(yearCapital, start=1):
    print(f"Año {i}: Capital obtenido ${capital:.2f}")
