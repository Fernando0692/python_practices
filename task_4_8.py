'''
Gandarilla Carrillo Fernando Christian
08/21/2023
Escribir un programa que permita gestionar la base de datos de clientes de una empresa. Los clientes se guardarán en un diccionario en donde la clave de cada cliente será su RFC, y  otro diccionario donde el valor seran los datos del cliente: nombre, dirección, teléfono, correo, preferente; donde tendrá el valor True si se trata de un cliente preferente. El programa debe preguntar al usuario por una opción del siguiente menú: (1) Añadir cliente, (2) Eliminar cliente, (3) Mostrar cliente, (4) Listar todos los clientes, (5) Listar clientes preferentes, (6) Terminar. 

En función de la opción elegida el programa tendrá que hacer lo siguiente:

Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos.
Preguntar por el RFC del cliente y eliminar sus datos de la base de datos.
Preguntar por el RFC del cliente y mostrar sus datos.
Mostrar lista de todos los clientes de la base de datos con su RFC y nombre.
Mostrar la lista de clientes preferentes de la base de datos con su RFC y nombre.
Terminar el programa.
Debe usar tantas funciones como sean necesarias.
'''

def add(bd):
    rfc = input("Ingrese el RFC del cliente: ")
    name = input("Ingrese el nombre del cliente: ")
    address = input("Ingrese la dirección del cliente: ")
    phone = input("Ingrese el teléfono del cliente: ")
    email = input("Ingrese el correo del cliente: ")
    isFavorite = input("¿Es un cliente preferente? (S/N): ").upper()
    isFavorite = isFavorite == "S" or isFavorite == "SI"
    
    data = {
        'nombre': name,
        'dirección': address,
        'teléfono': phone,
        'correo': email,
        'preferente': isFavorite
    }
    
    bd[rfc] = data
    print("Cliente agregado exitosamente.")

def delete(bd):
    rfc = input("Ingrese el RFC del cliente a eliminar: ")
    
    if rfc in bd:
        del bd[rfc]
        print("Cliente eliminado exitosamente.")
    else:
        print("Cliente no encontrado en la base de datos.")

def read(bd):
    rfc = input("Ingrese el RFC del cliente a mostrar: ")
    
    if rfc in bd:
        data = bd[rfc]
        print("\nDatos del cliente:")
        for id, value in data.items():
            print(f"{id.capitalize()}: {value}")
    else:
        print("Cliente no encontrado en la base de datos.")

def list(bd):
    print("\nLista de todos los clientes:")
    for rfc, data in bd.items():
        print(f"RFC: {rfc}, Nombre: {data['nombre']}")

def favorites(bd):
    print("\nLista de clientes preferentes:")
    for rfc, data in bd.items():
        if data['preferente']:
            print(f"RFC: {rfc}, Nombre: {data['nombre']}")

def end():
    print("Terminando el programa.")
    exit()

bd = {}

options = {
    '1': add,
    '2': delete,
    '3': read,
    '4': list,
    '5': favorites,
    '6': end
}

while True:
    print("\nMenú:")
    print("1. Agregar cliente")
    print("2. Eliminar cliente")
    print("3. Mostrar cliente")
    print("4. Lista de clientes")
    print("5. Lista de clientes preferentes")
    print("6. Terminar")
    
    opcion = input("Seleccione una opción (1-6): ")
    
    if opcion in options:
        options[opcion](bd)
    else:
        print("Opción inválida. Seleccione una opción válida del menú.")
