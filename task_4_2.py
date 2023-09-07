'''
Gandarilla Carrillo Fernando Christian
08/21/2023
Escribir un programa que almacene N asignaturas en una lista. Pregunte al usuario la nota que ha sacado en cada asignatura. Debe usar una lista de asignaturas y otra para las notas. Mostrar en pantalla:
En <asignatura> has sacado <nota>
'''

classes = [] 
score = []

try:
    n = int(input("Ingrese el número de asignaturas: "))
    if n >= 0:
        # Set elements on lists
        for i in range(n):
            className = input(f"Ingrese el nombre de la asignatura {i + 1}: ")
            classes.append(className)
            
            value = float(input(f"Ingrese la nota de {className}: "))
            score.append(value)
    else:
        print("La cantidad debe ser un valor entero.")
except ValueError:
    print("Ingrese un valor válido.")
    
    
    
    
# Print results
for i in range(n):
    print(f"En {classes[i]} has sacado {score[i]}")

