import numpy as np

consumo = np.array([
    [12.5, 13.2, 11.9, 14.0, 13.5, 15.0, 14.3],
    [10.1, 10.5, 10.0, 11.2, 11.5, 12.0, 11.8],
    [14.0, 14.2, 13.9, 15.5, 15.1, 16.0, 15.8],
    [9.0, 9.2, 8.9, 9.5, 9.8, 10.0, 9.7],
    [16.2, 16.5, 16.0, 17.1, 17.4, 18.0, 17.8],
    [11.0, 11.3, 11.1, 12.0, 12.4, 12.8, 12.5],
    [13.5, 13.8, 13.2, 14.1, 14.6, 15.0, 14.9],
    [10.8, 11.0, 10.6, 11.5, 11.8, 12.2, 12.0],
    [15.1, 15.5, 15.0, 16.0, 16.4, 17.0, 16.7],
    [8.5, 8.7, 8.4, 9.0, 9.2, 9.5, 9.3],
])

print ("Dimensiones:", consumo.ndim)
print ("Forma:", consumo.shape)
print ("Tipo de datos:", consumo.dtype)
print ("Consumo primer hogar", consumo[0])
print ("Consumo el miércoles (día 3):", consumo[:,2])

# Promedio de consumo por hogar
prom_por_hogar = np.mean(consumo, axis=1)

# Promedio de consumo diario de todos los hogares
prom_por_dia = np.mean(consumo, axis=0)

# Suma total de consumo en la semana de los 10 hogares
total_consumo = np.sum(consumo)

print (prom_por_hogar)
print (prom_por_dia)
print (total_consumo)

# Máximos por hogar
maximos = np.max(consumo, axis=1)

# Mínimo por día
mínimos = np.min(consumo, axis=0)

# Desviación estándar global
desviacion = np.std(consumo)

print (maximos)
print (mínimos)
print (desviacion)

# Suma por hogar (semana)
consumo_total_hogar = np.sum(consumo, axis=1)

# Índice del hogar con mayor consumo
hogar_mayor_consumo = np.argmax(consumo_total_hogar)

# índice del hogar con menor consumo
hogar_más_eficiente = np.argmin(consumo_total_hogar)

print(consumo_total_hogar)
print(hogar_mayor_consumo)
print(hogar_más_eficiente)

# Suma por hogar (semana)
consumo_total_hogar = np.sum(consumo, axis=1)
print(f"Consumo total de cada hogar durante la semana: {consumo_total_hogar}")

# Compara cada hogar con un valor mayor a 100
altos = consumo_total_hogar > 100
# Filtrando hogares que cumple la condición
consumo_mayor_100 = np.where(altos)[0]

print(f"IDs de hogares con cosumo mayor a 100: {consumo_mayor_100}")

# Aplicando normalización MinMax al conjunto de datos
consumo_normalizado = (consumo - consumo.min()) / (consumo.max() - consumo.min())

# Resultado
print (consumo_normalizado)

# 1. ¿Cuál es el consumo del hogar 5 el viernes (día 5)?
consumo_hogar5 = consumo[4, 4]
print(f"El consumo del hogar 5 el viernes es: {consumo_hogar5}")

# 2. Usando indexación, muestra el consumo de los últimos 3 hogares el domingo.
últimos_3hogares = consumo[7:, 6]
print(f"El consumo de los últimos 3 hogares el día domingo es {últimos_3hogares}")

# 3. Calcula el promedio de consumo los fines de semana (sábado y domingo, columnas 5 y 6).
prom_finde = np.mean(consumo, axis=0)[-2]
print (f"El promedio de consumo los fines de semana es de {prom_finde}")

# 4. ¿Qué día de la semana tiene la mayor desviación estándar entre hogares? Explica qué indica esto.
desv_por_dia = np.std(consumo, axis=0)
mayor_del_dia = np.argmax(desv_por_dia)

print (f"La desviación estándar entre los hogares por día es de  {desv_por_dia}")

semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
print (f"El día con mayor desviación estándar entre los hogares es {semana[mayor_del_dia]}")


# 5. Identifica los 3 hogares con menor consumo total durante la semana. Muestra sus índices y valores.
index_menor = np.argsort(consumo_total_hogar)[:3]
for i in index_menor:
    print (f"El hogar {i} tiene un consumo total de {consumo_total_hogar[i]}")

# 6. Si el hogar 3 aumenta su consumo en un 10% cada día, ¿cuál sería su nuevo consumo total semanal?
hogar3 = consumo[2]
new_hogar3= hogar3*1.1
print (f"El consumo del hogar 3 es de {hogar3}")
print (f"El comnsumo del hogar 3 aumentado en 10%  es de {new_hogar3}")