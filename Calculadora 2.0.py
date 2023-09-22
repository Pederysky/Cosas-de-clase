#Calculadora 2.0


while True:
    choice = input("Elige que operación deseas ejecutar (+ | - | * | /) (Pulsa c para cerrar el programa): ")
    if choice == 'c':
            break
    if choice in ('+', '-', '*', '/'):
        n1 = float(input("Dime el primer número: "))
        n2 = float(input("Dime el segundo número: "))
        if choice == '+':
            print(f"{n1} + {n2} = {n1+n2}")
        elif choice == '-':
            print(f"{n1} - {n2} = {n1-n2}")
        elif choice == '*':
            print(f"{n1} * {n2} = {n1*n2}")
        elif choice == '/':
            print(f"{n1} / {n2} = {n1/n2}")
            break
        

    else:
        print("El valor introducido no es válido")