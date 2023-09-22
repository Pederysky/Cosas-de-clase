peso = float(input("Introduce tu peso en kg: "))
estatura = float(input("Introduce tu estatura en metros: "))

imc = round(peso / (estatura ** 2), 2)

print("Tu IMC es: " + str(imc))


if imc <= 18.5:
    print("Tienes peso insuficiente")
       
elif imc <= 24.9:
    print("Estas en un peso ideal")
         
elif imc <= 29.9:
    print("Te está saliendo barriga, lleva cuidado")
        
elif imc >= 30.0:
    print("Tienes sobrepeso")
       
      
 
