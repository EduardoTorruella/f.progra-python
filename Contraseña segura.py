#Clase:        Clase 2
#Tema:         Bloque Condicional.
#Ejercicio:    2.3.1. Contraseña segura 
#Descripción:  Es un programa que solicita al usuario una contraseña la cual tiene que cumplir con ciertos requisitos como el tener más de 8 caracteres, tener mayúscular y números. 
#Fecha:        2025-05-16
#Estado:       [ Terminado ]


contra = input("Ingresa tu contraseña: ")

m= False
d= False
if len(contra) >= 8:
    for l in contra:
        if l.isdigit():
            d = True
        if l.isupper():
            m = True
    if d and m:
        print ("Contraseña segura")
    else:
       print ("Contraseña insegura")         
else:
    print ("Contraseña insegura")
