# 1. Escribe un programa que pida por teclado dos números enteros.
# A continuación, el programa debe calcular su división, escribiendo el cociente entero,
# en caso de que el resto no sea cero, habrá que mostrar también el valor del resto entero.

D = int(input("Introduce el Dividendo: "))
d = int(input("Introduce el Divisor: "))


if d <= 0:
    print("No se puede dividir entre 0")


else:
    cociente = D // d 
    resto = D % d 
    if resto == 0:
        print(f"La division es exacta. El cociente es {cociente} y el resto es {resto} ")
    else: 
        print(f"La division no es exacta. El cociente es {cociente} y el resto es {resto} ")
        
    