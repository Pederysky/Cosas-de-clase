numero=45 #Número que se desea adivinar
control=0 #variable de control de ciclo
intentos=1 #Controlar los intentos
print("Bienvenido al juego adivina un número")
while(control==0):
    print("Intento número: ",intentos)
    print("Ingrese número")
    num = int(input()) #Solicitamos un número para comparar
    if(num==numero):
        print("¡Adivinaste el número!")
        print("Utilizaste ",intentos," intentos-")
        print("Fin")
        control=1
    elif(num > numero):
        print("El número ingresado es mayor, prueba otra vez")
        intentos+=1
    elif(num < numero):
        print("El número ingresado es menor, prueba otra vez")
        intentos+=1