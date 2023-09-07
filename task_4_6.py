'''
Gandarilla Carrillo Fernando Christian
08/21/2023
Escribir un programa que guarde en una variable el diccionario {'Euro': valor en pesos, 'Dollar': valor en pesos, 'Yen': valor en pesos}, pregunte al usuario por una cantidad en pesos y muestre su conversión para cada una de las divisas.
'''

# Set currencies
currencies = {
    'Euro': 18.54,
    'Dollar': 16.99,
    'Yen': 0.12
}

# Set mexican pesos
pesos = float(input("Ingresa la cantidad en pesos: "))
    
for currency, value in currencies.items():
    valueConvert = pesos / value

    # Print result per each currency
    print("Cantidad en {}: {:.2f}".format(currency, valueConvert))
