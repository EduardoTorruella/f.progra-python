#Clase:        Clase 2
#Tema:         Bloque Condicional.
#Ejercicio:    2.3.2. Cálculo de impuesto.
#Descripción:  Es un programa que solicita al usuario las unidades de electricidad consumidas y depende en que rango estén, entonces se le aplicara cierta cantidad de impuesto. 
#Fecha:        2025-05-16
#Estado:       [ Terminado ]

u_consumo = float(input("Ingrese las unidades de consumo eléctrico: "))

if u_consumo >= 0  and  u_consumo <= 100:
    print ("El impuesto aplicado es $0.00")

elif u_consumo >= 101 and u_consumo <=200:
    impuesto = (u_consumo - 100) * 0.5
    print (f"El impuesto aplicado es ${impuesto}")

elif u_consumo >= 201:
    impuesto =  (100 * 0.5) + ((u_consumo - 200) * 0.7)
    print (f"El impuesto aplicado es ${impuesto}")
    
