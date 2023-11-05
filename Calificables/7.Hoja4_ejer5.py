# Escribe un programa que pida por pantalla un valor positivo. 
# A continuación, el programa pedirá números hasta que la suma de 
# todos los números introducidos supere el valor del número inicial, 
# mostrando el resultado de la suma.


n1 = float(input("Escribe la cantidad limite:"))

if n1<=0:
    print("MAAAAALLL. Introduce numeros positivos")
    exit()


contador = 0

i=1
while i<(n1+1):
    n2= float(input("Nuevo numero: "))
   
    if n2<=n1:
        contador+=n2
        #Este print sirve para comprobar que valor tiene la variable contador despues de cada input
        print (f"La suma actual de los numeros es: {contador}")
    elif contador==n1:
        print(f"Has realizado la suma correctamente. El total es {contador}")
    else:
        print(f"Te has pasado del limite. La suma actual es {contador}")
    
    i = i + 1