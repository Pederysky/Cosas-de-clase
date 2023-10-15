# 3. HOJA EJERCICIOS 4. EJERCICIO 8. Escribe un programa que permita sumar números, 
# la aplicación debe funcionar de la siguiente forma:
#  a. En primer lugar, el programa preguntará por la cantidad de números que se van a introducir
#  b. A continuación, el programa debe pedir cada uno de esos valores (pueden ser decimales). 
#  c. Por último, el programa calculará el número mayor, el menor, la suma y la media de todos ellos 
# y mostrará el resultado por pantalla. 
# Ten en cuenta que sólo mostraremos 2 decimales.

nums = int(input("¿Cuántos valores vas a introducir?: "))

suma = 0 
mayor = 0
menor = 0

for i in range (nums):
    valor = float(input(f"Introduce el número {i+1}: "))
    suma = suma + valor
    if i == 0:
        mayor = valor
        menor = valor
    else:
        if mayor < valor:
            mayor = valor
        if menor > valor:
            menor = valor

print(f"El valor mayor es {mayor}")
print(f"El valor menor es {menor}")

print(f"La suma de los valores es {suma}")

media = suma / nums
print(f"La media es {media}")

