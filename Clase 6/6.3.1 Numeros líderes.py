#Clase:        Clase 6
#Tema:         Manejo de lista
#Ejercicio:    6.3.1 Numeros líderes 
#Descripción:  Es un programa que evalua si un numero es mayor al los que le siguen, se considerará como un número líder.
#Fecha:        2025-05-30
#Estado:       [ Terminado ]

lista = input("Ingrese la lista que desee: ")
lst = lista.split()
lst2 = []
for n in lst:
    lst2.append(int(n))


lideres= []

for i in range(len(lst2)):
    numlid = True
    for j in range(i+1, len(lst2)):
        if lst2[i] <= lst2[j]:
            numlid = False
            break
    if numlid:
        lideres.append(lst2[i])    

for num in lideres:
    print (num, end= " ")
