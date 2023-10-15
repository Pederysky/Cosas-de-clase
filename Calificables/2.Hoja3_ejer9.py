# Escribe un programa que en primer lugar pregunte si se quiere calcular 
# el área de un triángulo o la de un círculo.
# Si se contesta que se quiere calcular el área de un triángulo, 
# el programa tiene que pedir entonces la base y la altura y escribir el área.
# Si se contesta que se quiere calcular el área de un círculo, 
# el programa tiene que pedir entonces el radio y escribir el área.
# En ambos casos el programa debe ser capaz de calcular y mostrar el resultado 
# adecuado.

#importamos solo pi para consumir menos memoria
from math import pi

while True:
    choice = input("¿Que quieres calcular? Pulsa 'T' para el área de un triángulo o "+
                   "pulsa 'C' para el área de un círculo. (También puedes pulsar 'E'"+
                   " para cerrar   el programa)").upper()
    if choice == 'E':
            break
    if choice in ('T'):
          base = float(input("Dime la base del triángulo: "))
          altura = float(input("Dime la altura del triángulo: "))
          aT = (base * altura) / 2
          print(f"El área del triángulo es {aT}")
    elif choice in ('C'):
          radio = float(input("Dime el radio del círculo: "))
          aC = pi * (radio ** 2)
          print(f"El área del círculo es {aC}")