# ============================================================
# Analizador de texto
# ============================================================

# ------------------------------------------------------------
# ENTRADA DE DATOS
# ------------------------------------------------------------
texto = input("Ingresa tu texto: ").lower()
ingresa = input("Ingresa tres letras: ").lower()

# Guardamos las letras en una lista eliminando posibles espacios
letras = list(ingresa.replace(" ", ""))
print(f"\nTus letras elegidas son: '{letras[0]}', '{letras[1]}' y '{letras[2]}'")

# ------------------------------------------------------------
# 1. Conteo de apariciones de cada letra
# ------------------------------------------------------------
conteo_1 = texto.count(letras[0])
conteo_2 = texto.count(letras[1])
conteo_3 = texto.count(letras[2])

print(
    f"\n- La letra '{letras[0]}' aparece {conteo_1} veces."
    f"\n- La letra '{letras[1]}' aparece {conteo_2} veces."
    f"\n- La letra '{letras[2]}' aparece {conteo_3} veces."
)

# ------------------------------------------------------------
# 2. Número total de palabras
# ------------------------------------------------------------
palabras_texto = texto.split()
longitud_texto = len(palabras_texto)
print(f"\nTu texto tiene {longitud_texto} palabras.")

# ------------------------------------------------------------
# 3. Primera y última letra del texto
# ------------------------------------------------------------
primera_letra = texto[0]
ultima_letra = texto[-1]
print(f"La primera letra de tu texto es '{primera_letra}' y la última es '{ultima_letra}'.")

# ------------------------------------------------------------
# 4. Texto con el orden de las palabras invertido
# ------------------------------------------------------------
palabras_texto.reverse()
texto_invertido = " ".join(palabras_texto)
print(f"\nTu texto con las palabras invertidas es:\n{texto_invertido}")

# ------------------------------------------------------------
# 5. Búsqueda de la palabra "Python" mediante diccionario
# ------------------------------------------------------------
buscar_python = "python" in texto
diccionario = {True: "sí", False: "no"}
print(f"\nLa palabra 'Python' {diccionario[buscar_python]} se encuentra en el texto.")