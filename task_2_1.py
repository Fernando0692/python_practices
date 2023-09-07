'''
Gandarilla Carrillo Fernando Christian
08/18/2023
Actividad 2.1 Escribir el codigo que permita Pedir la hora al usuario (solo debe ser la hora), convertir en minutos, segundos, milisegundos e imprimir cada resultado con el mesaje correspondiente. Deberá incluir  incluir  comentarios necesarios para documentar el codigo y su nombre.
'''

hour = input('Escribe la hora a convertir (formato 24hrs):')

# Se calculan los minutos
total_minutos = int(hour) * 60
# Se calculan los segundos
total_segundos = int(hour) * 3600
# Se calculan los milisegundos
total_milisegundos = int(hour) * 3600000

# Imprimimos los resultados con mensajes descriptivos
print("La hora ingresada en minutos es:", total_minutos, "minutos")
print("La hora ingresada en segundos es:", total_segundos, "segundos")
print("La hora ingresada en milisegundos es:", total_milisegundos, "milisegundos")