# ============================================================
#  LABORATORIO DÍA 3 · Organizador de una playlist para un viaje
#  Uso de strings, listas, diccionarios, tuplas y sets
# ============================================================

# Datos iniciales de la playlist
canciones_texto = "Ruta del sol,Mar abierto,Noches de radio,Ciudad dormida"
duraciones = {
    "Ruta del sol": 215,
    "Mar abierto": 198,
    "Noches de radio": 240,
    "Ciudad dormida": 185,
}
datos_playlist = ("Viaje al sur", "Ana", 2026)
generos_ana = {"rock", "pop", "indie"}
generos_luis = {"pop", "jazz", "reggae"}

# ------------------------------------------------------------
# 1. Conversión de texto a lista de canciones
# ------------------------------------------------------------
lista_canciones = canciones_texto.split(",")
print(lista_canciones)
print(f"Total de canciones: {len(lista_canciones)}")

# ------------------------------------------------------------
# 2. Modificación y ordenación de la lista
# ------------------------------------------------------------
cancion_nueva = input("\nIngresa una canción nueva a la lista de canciones: ")

lista_canciones.append(cancion_nueva)
lista_canciones.sort()
print(lista_canciones)
print(f"Canción eliminada: {lista_canciones.pop()}")

# ------------------------------------------------------------
# 3. Operaciones sobre la primera canción y unión de la lista
# ------------------------------------------------------------
primera_cancion = lista_canciones[0]

print(f"\nMayúsculas: {primera_cancion.upper()}")
print(f"Tres primeras letras: {primera_cancion[:3]}")
print(f"Al revés: {primera_cancion[::-1]}")
print(f"Cantidad de letras 'a': {primera_cancion.count('a')}")
print(" | ".join(lista_canciones))

# ------------------------------------------------------------
# 4. Diccionario de duraciones y cálculo de minutos/segundos
# ------------------------------------------------------------
duracion_cancion_nueva = int(
    input(f"\nIngresa la duración de '{cancion_nueva}' en segundos: ")
)

duraciones[cancion_nueva] = duracion_cancion_nueva
print(duraciones.keys())
print(duraciones.values())

mar_abierto_minutos = duraciones["Mar abierto"] // 60
mar_abierto_segundos = duraciones["Mar abierto"] % 60
print(f"Mar abierto dura {mar_abierto_minutos} min y {mar_abierto_segundos} s")

# ------------------------------------------------------------
# 5. Desempaquetado de tupla
# ------------------------------------------------------------
nombre, autora, anio = datos_playlist
print(f"\nLa playlist {nombre} fue creada por {autora} en {anio}")

# ------------------------------------------------------------
# 6. Operaciones con sets y comprobación booleana
# ------------------------------------------------------------
generos_union = generos_ana.union(generos_luis)
generos_union.add("folk")
generos_union.discard("reggae")

print(f"\nGéneros finales: {generos_union}")
print(f"Total de géneros: {len(generos_union)}")
print(f"¿Está 'jazz' en la lista?: {'jazz' in generos_union}")