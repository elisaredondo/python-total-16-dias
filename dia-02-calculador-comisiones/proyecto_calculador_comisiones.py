# Proyecto - Día 2: Calculador de comisiones
print("---------------------------------")
print("Programa para calcular comisiones")
print("---------------------------------")

#variables
nombre =  input("¿Cuál es tu nombre?: ")
ingresos =  float(input("¿Cuáles son las ventas de este mes?: "))

#El vendedor se lleva 13% de comisión
comision =  round(0.13 * ingresos,2)

print(f"Enhorabuena, {nombre}, la comisión de tus ventas totales es: {comision} €")