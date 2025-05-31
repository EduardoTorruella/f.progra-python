#Clase:        Clase 5
#Tema:         Bucles for y while
#Ejercicio:    5.4.1. ¡Adivina el número!
#Descripción:  Es un programa que genera un número aleatorio entre 1 y 100 y pide al usuario que lo adivine. El programa sigue pidiendo números hasta que acierte. 
#              En cada intento fallido el programa notificará al usuario si el número secreto es mayor o menor al último valor ingresado.
#Fecha:        2025-05-28
#Estado:       [ Terminado ]

import random


numero = random.randint(1, 100)

num = int(input("Ingrese un número del 1 al 100: "))

while num != numero:
    if numero > num:
        print ("El número secreto es mayor")
        num = int(input("Ingrese un número del 1 al 100: "))
    elif numero < num:
        print ("El número secreto es menor")
        num = int(input("Ingrese un número del 1 al 100: "))
    
print ("¡Felicidades! Has adivinado el número secreto")
print ("Fin del juego")