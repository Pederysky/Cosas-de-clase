suma = 0

while True:
    # Solicita al usuario que introduzca un número
    entrada = input("Introduce un número (o 'q' para salir): ")

    # Comprueba si el usuario quiere salir del bucle
    if entrada.lower() == 'q':
        break

    try:
        # Convierte la entrada a un número (puedes manejar errores aquí)
        numero = float(entrada)
        # Suma el número a la variable suma
        suma += numero
    except ValueError:
        print("Entrada no válida. Introduce un número válido o 'q' para salir.")

# Muestra la suma total
print("La suma total es:", suma)