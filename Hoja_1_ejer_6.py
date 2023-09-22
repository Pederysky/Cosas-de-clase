# #Escribir un programa que pida al usuario dos números enteros y 
# muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> 
# son los números introducidos por el usuario, 
# y <c> y <r> son el cociente y el resto de la división entera respectivamente.


n = int(input("Introduce Numero 1: "))
m = int(input("Introduce Numero 2: "))
# + - / *  **(potencia)  //division entera %resto


cociente = (n//m)
resto = n%m
print(f"El cociente es: {cociente} y el resto es {resto}")