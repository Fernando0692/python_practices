'''
Gandarilla Carrillo Fernando Christian
08/21/2023
Escribir un programa  que calcule el promedio de una materia donde los examenes tienen un valor del 25%, las tareas 25% y el trabajo final 50%. La cantidad de examenes que se aplican en el curso son tres y  la cantidad de tareas que realizan son cuatro.  La calificacion minima para acredicar el curso es 70. Debera indicar si aprobo o no el curso.
'''

# Read marks from tests
tests = []
for i in range(3):
    value = float(input(f"Ingrese la calificación del examen {i+1}: "))
    tests.append(value)

# Read marks from tasks
tasks = []
for i in range(4):
    value = float(input(f"Ingrese la calificación de la tarea {i+1}: "))
    tasks.append(value)

# Read mark from final project
project = float(input("Ingrese la calificación del trabajo final: "))

# Calc for prom
prom = ((sum(tests) / 3) * 0.25) + ((sum(tasks) / 4) * 0.25) + (project * .5)

if prom >= 70:
    result = "Aprobado"
else:
    result = "No aprobado"

# Print final grade
print(f"Promedio: {prom:.2f}")
print(f"Resultado: {result}")
