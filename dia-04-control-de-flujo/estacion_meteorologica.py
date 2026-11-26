from random import choice, randint

# Datos semanales de entrada
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
temperaturas = [18.5, 22.0, 25.5, 30.5, 27.0, 16.5, 21.0]

# 1. Emparejar días y temperaturas con zip()
tem_semana = list(zip(dias, temperaturas))

for dia, tem in tem_semana:
    print(f"{dia}: {tem} °C")

# 2. Calcular mínima, máxima y localizar el día más caluroso
minima = min(temperaturas)
maxima = max(temperaturas)

print(f"\nTemperatura mínima: {minima} °C")
print(f"Temperatura máxima: {maxima} °C")

for dia, grado in zip(dias, temperaturas):
    if grado == maxima:
        print(f"La temperatura más alta se registró el {dia} ({grado} °C)")

# 3. Clasificar cada día según su rango térmico
print()
for dia, grado in zip(dias, temperaturas):
    if grado < 20:
        print(f"{dia}: frío")
    elif grado <= 27:
        print(f"{dia}: templado")
    else:
        print(f"{dia}: caluroso")

# 4. Filtrar días > 20 °C con comprensión de listas y calcular promedio semanal
temperaturas_mayor_20 = [grado for grado in temperaturas if grado > 20]
print(f"\nTemperaturas mayores a 20 °C: {temperaturas_mayor_20} (Total: {len(temperaturas_mayor_20)} días)")

valor = 0
for grado in temperaturas:
    valor += grado

promedio = round(valor / len(temperaturas), 1)
print(f"Promedio semanal: {promedio} °C")

# 5. Numerar los días con enumerate() y simular pronóstico aleatorio
print()
cielo = ["soleado", "nublado", "lluvioso"]

for indice, dia in enumerate(dias):
    print(f"El {dia} es el día {indice + 1}")

cielo_aleatorio = choice(cielo)
temp_aleatoria = randint(15, 30)
print(f"El pronóstico de mañana es un cielo {cielo_aleatorio} con una temperatura de {temp_aleatoria} °C")

# 6. Menú interactivo con bucle while y coincidencia de patrones (match/case)
while True:
    print("\n--- MENÚ ---")
    print("1) Consultar un día")
    print("2) Ver el promedio")
    print("3) Salir")
    opcion = input("Elige una opción: ")

    match opcion:
        case "1":
            dia_consulta = input("Escribe el nombre del día: ").capitalize()
            if dia_consulta in dias:
                posicion = dias.index(dia_consulta)
                print(f"La temperatura del {dia_consulta} es {temperaturas[posicion]} °C")
            else:
                print("Ese día no está en la lista.")
        case "2":
            print(f"El promedio semanal es {promedio} °C")
        case "3":
            print("Saliendo...")
            break
        case _:
            print("Opción inválida")