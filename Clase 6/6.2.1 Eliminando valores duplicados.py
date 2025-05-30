#Clase:        Clase 6
#Tema:         Manejo de lista
#Ejercicio:    6.2.1 Eliminando valores duplicados 
#Descripción:  Es un programa que solicita al usuario una lista y la recorre, eliminando los valores duplicados y dejando solamente la primera vez que aprecen en la lista.
#Fecha:        2025-05-30
#Estado:       [ Terminado ]

l = input("Ingrese la lista que desee: ")

lst = l.split()

nwlst = []

for num in lst:
    int(num)
    if num not in nwlst:
        nwlst.append(num)
for n in nwlst:
    print (n, end=" ")


