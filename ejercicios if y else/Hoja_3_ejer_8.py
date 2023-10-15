import math

a = float(input("Introduce el valor del coeficiente a: "))
b = float(input("Introduce el valor del coeficiente b: "))
c = float(input("Introduce el valor del coeficiente c: "))
print(f"Ecuación {a} x² + {b} x+ {c} = 0")

raiz_cuadrada = (((b ** 2) - (4 * (a * c))))
print(raiz_cuadrada)
if raiz_cuadrada <0:
    print("Sin solución real")
elif a == b == c == 0:
    print("Todos los números son solución")
else:

    operacion = math.sqrt(raiz_cuadrada)
    resultado1 = (((-1) * b) + operacion) / (2 * a)
    resultado2 = (((-1) * b) - operacion) / (2 * a)

    if resultado1 == resultado2:
        print(f" El único resultado es: {resultado1}")

    else:
        operacion = math.sqrt(raiz_cuadrada)
        resultado1 = (((-1) * b) + operacion) / (2 * a)
        resultado2 = (((-1) * b) - operacion) / (2 * a)
        print("El resultado puede ser " + str(resultado1) + " o " + str(resultado2))