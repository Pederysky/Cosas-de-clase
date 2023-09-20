

#Operaciones 

def suma(n1, n2):
    return n1 + n2
def resta(n1, n2):
    return n1 - n2
def multiplicacion(n1, n2):
    return n1 * n2
def division(n1, n2):
    return n1 / n2

#Calculadora


while True:
    choice = input("Elige que operación deseas ejecutar (+ | - | * | /): ")
    if choice in ('+', '-', '*', '/'):
        n1 = float(input("Dime el primer número: "))
        n2 = float(input("Dime el segundo número: "))
        if choice == '+':
            print(f"{n1} + {n2} = ", suma(n1, n2))
        elif choice == '-':
            print(f"{n1} - {n2} = ", resta(n1, n2))
        elif choice == '*':
            print(f"{n1} * {n2} = ", multiplicacion(n1, n2))
        elif choice == '/':
            print(f"{n1} / {n2} = ", division(n1, n2))
            break

    else:
        print("El valor introducido no es válido")