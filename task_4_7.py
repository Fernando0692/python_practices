'''
Gandarilla Carrillo Fernando Christian
08/21/2023
Escribir un programa que cree un diccionario simulando una cesta de la compra. El programa debe preguntar el artículo y su precio y añadir el par al diccionario, hasta que el usuario decida terminar. Después se debe mostrar por pantalla la lista de la compra y el coste total, con el siguiente formato:
Lista de la compra
Artículo    Precio
Artículo    Precio
Artículo    Precio
…                …
Total:  $ XX.XX

'''
# Object (dictionary) to shop list
shopList = {}
    
# Start loop to set each item on shop list
while True:
    item = input("Ingresa el nombre del artículo (o 'stop/teminar' para finalizar la lista): ")

    # Set stop to loop
    if item.lower() == "terminar" or item.lower() == "stop":
        break

    # Set price to item
    price = float(input("Ingresa el precio del artículo: "))
    shopList[item] = price

# Print headers
print("\nLista de la compra")
print("Artículo --- Precio")

# Print items for shop list
total = 0
for item, price in shopList.items():
    print("{:<12} {:.2f}".format(item.capitalize(), price))
    total += price

# Print totals
print("\nTotal: ${:.2f}".format(total))
