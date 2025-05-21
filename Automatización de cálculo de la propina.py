#Clase:        Clase 1
#Tema:         Fundamentos
#Ejercicio:    1.3.1 Automatizando el cálculo de la propina
#Descripción:  Es un programa que solicita al usuario el total de su cuenta, luego el porcentaje de propina, luego se calcula la propina como tal y se le suma al total de la cuenta.
#Fecha:        2025-05-14
#Estado:       [ Terminado ]

tot = float(input("Ingresa el total de la cuenta: "))
porcentaje_prop = float(input("Ingresa el porcentaje de propina: "))
propina = tot * (porcentaje_prop / 100)

totpropina = tot + propina

print ()
print (f'El total de la cuenta es de: ${tot}')
print (f'La propina es de: ${propina}')
print (f'El total de la cuenta con la propina es de: ${totpropina}')