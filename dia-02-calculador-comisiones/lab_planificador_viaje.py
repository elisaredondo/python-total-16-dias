# Laboratorio Evaluado - Día 2: Planificador de un viaje en auto

# Paso 1: Datos del viaje
destino = input("Destino del viaje: ")
distancia = int(input("Distancia en Km: "))
precio = float(input("Precio de combustible: "))

# Paso 2: Tipos de datos
print(type(distancia))
print(type(precio))

# Paso 3: Combustible
litros_necesarios = (distancia * 8) / 100
costo_combustible = round(litros_necesarios * precio, 2)

# Paso 4: Duración
duracion = distancia * 60 // 90
horas = duracion // 60
minutos = duracion % 60

# Paso 5: Cuentas extra
precio_persona = round(costo_combustible / 4, 2)
precio_persona_10 = round(costo_combustible * 1.1 ** 3, 2)

# Paso 6: Resumen
print(f"Destino: {destino}")
print("Litros necesarios: {}".format(litros_necesarios))
print(f"Costo del combustible: ${costo_combustible}")
print(f"Duración: {horas} h {minutos} min")
print(f"Cada uno paga: ${precio_persona}")
print(f"En 3 años costaría: ${precio_persona_10}")