#Realiza la descomposición en factores primos de un número dado por teclado.

n1 = int(input("Escribe un número entero mayor que 1:"))

if n1<=1:
    print(f"{n1} no es mayor que 1")
    exit()
divisor=2

print("Descomposicion en factores primos: ")

while divisor <= n1:
        if n1 % divisor == 0:
            n1 = n1 // divisor
            print(f"{divisor}",end=" ")
        else:
            divisor += 1

