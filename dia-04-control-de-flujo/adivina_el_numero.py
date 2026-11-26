from random import randint

# Configuración inicial de la partida
nombre = input("¿Cómo te llamas?: ")
secreto = randint(1, 100)
intentos = 0

print(f"Bueno, {nombre}, he pensado un número entre 1 y 100, y tienes solo ocho intentos para adivinar cuál crees que es.")

# Bucle principal limitado a un máximo de 8 intentos válidos
while intentos < 8:
    # Mensaje dinámico según sea el primer intento o uno posterior
    if intentos == 0:
        numero_usuario = int(input("¿Cuál crees que es el número?: "))
    else:
        numero_usuario = int(input("Prueba otra vez: "))

    # Validación de rango y comprobación frente al número secreto
    if numero_usuario < 1 or numero_usuario > 100:
        print("Has elegido un número que no está permitido (debe estar entre 1 y 100).")
    elif numero_usuario < secreto:
        intentos += 1
        print(f"Incorrecto, has elegido un número menor al número secreto. Te quedan {8 - intentos} intentos.")
    elif numero_usuario > secreto:
        intentos += 1
        print(f"Incorrecto, has elegido un número mayor al número secreto. Te quedan {8 - intentos} intentos.")
    else:
        intentos += 1
        print(f"¡ENHORABUENA, {nombre}! Lo has adivinado en {intentos} intentos.")
        break
else:
    # Se ejecuta solo si el bucle termina sin haber alcanzado un break
    print(f"Se han agotado los 8 intentos. El número secreto era el {secreto}.")