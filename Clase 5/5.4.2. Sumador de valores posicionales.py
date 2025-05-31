#Clase:        Clase 5
#Tema:         Bucles for y while
#Ejercicio:    5.4.2. Sumador de valores posicionales
#Descripción:  Es un programa que pide un número al usuario y suma sus dígitos hasta que quede un solo dígito.Ejemplo:
#              Si el usuario ingresa 9875, entonces: 9+8+7+5 = 29 → 2+9 = 11 → 1+1 = 2.
#Fecha:        2025-05-28
#Estado:       [ Terminado ]

while True:
    num = int(input("Ingresa un número: "))

    while num >= 10:
        contador = 0
        for n in str(num):
            contador += int(n)
        num = contador
    print (f"El resultado final es {contador}")