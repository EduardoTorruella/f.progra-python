#Clase:        Clase 10
#Tema:         Manejo de matrices
#Ejercicio:    10.3.1. Matriz simétrica
#Descripción:  Es un programa que solicita al usuario una matriz, la recorre y enceuntra su diagonal principal, luego verifica e imprime si es una matriz simétrica o no.
#Fecha:        2025-06-09
#Estado:       [ Terminado ]

N = int(input())
m =  []
for i in range(N):
    temp = list(map(int, input().split(",")))
    m.append(temp)

diagonal_p = []

for i in range(len(m)):
    for j in range(len(m[i])):
        if i == j:
            diagonal_p.append(m[i][j])

simetria = True
for f in range(len(m)):
    for c in range(len(m[f])):
        if m[f][c] == m[c][f]:
            continue
        else:
            simetria = False
            break 

if simetria:
    print ("La amtriz es simétrica")
else:
    print ("La amtriz no es simétrica")

