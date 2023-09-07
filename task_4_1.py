'''
Gandarilla Carrillo Fernando Christian
08/21/2023
Escribir un programa que almacene N asignaturas de un curso en una lista. Muestre en pantalla el mensaje: Yo estudio <asignatura>, donde <asignatura> es cada una de las asignaturas de la lista.
'''

classes = [] 
try:
    n = int(input("Ingrese el número de asignaturas: "))
    if n >= 0:
        # Set element to list
        for i in range(n):
            className = input(f"Ingrese el nombre de la asignatura {i + 1}: ")
            classes.append(className)
    else:
        print("La cantidad debe ser un valor entero.")
except ValueError:
    print("Ingrese un valor válido.")



# Print results
for className in classes:
    print("Yo estudio", className)
