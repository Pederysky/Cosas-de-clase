# Realiza un programa que calcule las raíces de un polinomio de 2º grado.
# Nota: un polinomio de 2º grado es de la siguiente:
# ax2 + bx1  + c =  0.
# y su fórmula  Para ello debemos leer los valores a, b y c y aplicar las formulas. Recordad que tiene dos soluciones. 

import math

a = int(input("Introduce el monomio con potencia 2: "))
b = int(input("Introduce el monomio: "))
c = int(input("Introduce el número entero: "))

raiz_cuadrada = (((b ** 2) - (4 * (a * c))))
print(raiz_cuadrada)
operacion = math.sqrt(raiz_cuadrada)
resultado1 = (((-1) * b) + operacion) / (2 * a)
resultado2 = (((-1) * b) - operacion) / (2 * a)
print("El resultado puede ser " + str(resultado1) + " o " + str(resultado2))









