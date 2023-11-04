# Crea un programa que permita calcular superficies de cualquier tipo de cuadrado, rectángulo, trapecio, triángulo, círculo y romboide. 
# El programa mostrará un menú inicial con las distintas opciones, solicitará los valores necesarios, 
# calculará el resultado utilizando la función necesaria definida en el ejercicio anterior y mostrará el resultado por pantalla.
from math import pi

while True:
    print("Selecciona una opción")
    print("a) Superficie de un cuadrado")
    print("b) Superficie de un rectángulo")
    print("c) Superficie de un trapecio")
    print("d) Superficie de un triángulo")
    print("e) Superficie de un círculo")
    print("f) Superficie de un romboide")
    opcion = input("Elige una opción ").lower()

#Cuadrado
    if opcion == "a":
        lado = float(input("Dime lo que mide el lado: "))
        aCuadrado = lado * lado
        print (f"El área del cuadrado es {aCuadrado}")
        break
#Rectángulo
    elif opcion == "b":
        base = float(input("Dime la base del rectángulo: "))
        altura = float(input("Dime la altura del rectángulo: "))
        aR = base * altura
        print (f"El área del rectángulo es {aR}")
        break
#Trapecio
    elif opcion == "c":
        base1 = float(input("Dime la base superior: "))
        base2 = float(input("Dime la base inferior: "))
        h = float(input("Dime la altura: "))
        aTrapecio = ((base1 + base2) * h) / 2
        print (f"El área del trapecio es {aTrapecio}")
        break
#Triángulo
    elif opcion == "d":
        base = float(input("Dime la base del triángulo: "))
        altura = float(input("Dime la altura del triángulo: "))
        aT = (base * altura) / 2
        print(f"El área del triángulo es {aT}")
        break
#Círculo
    elif opcion == "e":
        radio = float(input("Dime el radio del círculo: "))
        aC = pi * (radio ** 2)
        print(f"El área del círculo es {aC}")
        break
#Romboide
    elif opcion == "f":
        base = float(input("Dime la base del romboide: "))
        altura = float(input("Dime la altura del romboide: "))
        aRomboide = base * altura
        print (f"El área del r es {aRomboide}")
        break
    else:
        print("Opcion no valida.")