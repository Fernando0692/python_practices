'''
Gandarilla Carrillo Fernando Christian
08/21/2023
Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A está formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte la primera letra de su nombre y sexo (F/M), y muestre por pantalla el grupo que le corresponde.
'''

# Get initial name & gender
initial = input("Ingresa la primera letra de tu nombre: ")
gender = input("Ingresa tu sexo (F/M): ")
group = ''

# Check which group is the ideal
if (gender == "F" and initial <= "M") or (gender == "M" and initial >= "N"):
    group = "A"
else:
    group = "B"



# Print result:
print("Tu grupo es: ", group)
