
#Clase:        Clase 1
#Tema:         Fundamentos
#Ejercicio:    1.3.2 Generador de correo de Key 
#Descripción:  Es un programa que solicita al usuario su nombre y luego genera su correo de Key con el formato primer_nombre.primer_apellido@keyinstitute.edu.sv
#Autor:        Eduardo Torruella
#Fecha:        2025-05-14
#Estado:       [ Terminado ]

nombre = input("Ingresa tu nombre: ")
apellido = input ("Ingresa tu apellido: ")


print (f"{nombre.lower()}.{apellido.lower()}@keyinstitute.edu.sv")
