# import random
# numero = random (1,100)
# funciones core (vienen cargadas en el sistema)
# print("texto")
# input("texto")
# int("texto")


#funciones nivel 2 (no vienen cargadas en el sistema, pero si estan en python)
# from math import sqrt
# n= sqrt(69)

# 2 nivel 3
#A)  Funciones que instalo/importo
#B)  Funciones personalizadas 


#Funcion calcular el factorial
def factorial(numero):
    solucion=1
    for i in range (1, numero+1):
        solucion=solucion*i
    return solucion



#Funcion comprobar si es primo
def primo(num):
        for i in range(2, num):
            if num % i == 0:
               return False
        return True
                

#Funcion Calcula el maximo de 3
def MaximodeTres(n1,n2,n3):
    if n1>n2 and n1>n3:
        maximo = n1
    elif n2>n1 and n2>n3:
        maximo = n2
    else:
        maximo = n3
    return maximo
