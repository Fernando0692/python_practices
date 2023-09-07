'''
Gandarilla Carrillo Fernando Christian
08/21/2023
En una determinada empresa, sus empleados son evaluados cada seis meses. Los puntos que pueden obtener en la evaluación comienzan en 0 y pueden ir aumentando hasta llegar a 10, traduciéndose en mejores beneficios. Al final del problema se muestra una tabla con los niveles correspondientes a cada puntuación. La cantidad de dinero conseguida en cada nivel  se calcula multiplicando el salario mensual por la  división de la puntuación del nivel divida entre 10. Escribir un programa que lea la puntuación del usuario y su salario mensual e imprima su nivel de rendimiento, así como la cantidad de dinero que recibirá el usuario. 

Ejemplo: Salario 10,000; Puntuación 8. Dinero = 10,000 * (8/10)= 8000. 
Resultado: Nivel de Rendimiento Meritorio, Cantidad de Dinero Recibido $8000. 

Nivel --------------Puntuación
Inaceptable ---------  0 a 3
Aceptable------------  4 a 6
Meritorio ------------- 7 a 10
'''

# Variables to set salary, points && one empty to set level of performance
salary = float(input("Ingresa tu salario mensual: "))
points = float(input("Ingresa tu puntuación: "))
lvl = ''

if points >= 0 and points <= 3:
    lvl = "Inaceptable"
elif points <= 6:
    lvl = "Aceptable"
else:
    lvl = "Meritorio"

bonus = salary * (points / 10)

# Print results
print("Nivel de Rendimiento ", lvl)
print("Dinero Recibido ${:.2f}".format(bonus))
