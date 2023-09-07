'''
Gandarilla Carrillo Fernando Christian
08/21/2023
Adivina Número. La computadora debe generar un número aleatorio entre 1 a 30 que el usuario intentará adivinar.  Tiene 5 intentos para coincidir con la computadora. En cada intento debe pedir elegir UN  número entre 1 a 30. Cada que introduzca un número indicará si esté es menor o mayor al elegido por la computadora. Si el número de intentos llega a cero debe imprimir game over, en caso contrario mostrar un mensaje de felicitación por ganar el juego.

IMPORTANTE: Para generar números aleatorios deberá importar la librería random usango lo siguiente: import random  al inicio de su programa. La función a utilizar es  num_compu = random.randint(1, 30)

Cuando gane debera romper el ciclo
'''
import random

num_compu = random.randint(1, 30)  # create randum number (1-30)
trys = 5  # Número de intentos disponibles

while trys > 0:
    num_usr = int(input("Intenta adivinar el número (entre 1 y 30): "))
    
    if num_usr == num_compu:
        print("¡Felicitaciones! ¡Adivinaste el número!")
        break
    elif num_usr < num_compu:
        print("El número es mayor. Te quedan {} intentos.".format(trys - 1))
    else:
        print("El número es menor. Te quedan {} intentos.".format(trys - 1))
    
    trys -= 1

if trys == 0:
    print("¡Game over! El número era {}.".format(num_compu))

