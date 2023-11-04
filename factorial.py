#5!=1x2x3x4x5=120
#6!=1x2x3x4x5x6=720

def factorial(numero):
    solucion=1
    for i in range (1, numero+1):
        solucion=solucion*i
    return solucion


numero = int(input("Introduce un numero: "))

# resultado=1
# for i in range (1, numero+1):
#     resultado=resultado*i

resultado = factorial (numero)














print (f"El factorial de {numero} es {resultado}")