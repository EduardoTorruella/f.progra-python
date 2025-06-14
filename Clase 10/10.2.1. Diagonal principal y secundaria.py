#Clase:        Clase 10
#Tema:         Manejo de matrices
#Ejercicio:    10.2.1. Diagonal principal y secundaria
#Descripción:  Es un programa que solicita al usuario ingresar los datos para crear una matriz, recorre la matriz e imprime la diagonal principal (izquierda a derecha) y la diagonal secundaria (de derecha a izquierda).
#Fecha:        2025-06-09
#Estado:       [ Terminado ]

N = int(input())
l =  []
for i in range(N):
    temp = list(map(int, input().split(",")))
    l.append(temp)


dp = []
ds =[]

for i in range(len(l)):
    for j in range(len(l[i])):
        if i == j:
            dp.append(l[i][j])
            
        if i + j == len(l)-1:
            ds.append(l[i][j])

print (dp)
print (ds)