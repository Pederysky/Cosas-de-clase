peso = float(input("Introduce tu peso en kg: "))
estatura = float(input("Introduce tu estatura en metros: "))

imc = round(peso / (estatura ** 2), 2)

print("Tu IMC es: " + str(imc))


if imc <= 18.5:
       peso = "Tienes peso insuficiente"
       return peso
elif imc <= 24.9:
     peso = "Estas en un peso ideal"
     return peso
elif imc <= 29.9:
      peso = "Te está saliendo barriga, lleva cuidado"
      return peso
elif imc >= 30.0:
      peso = "Tienes sobrepeso"
      return peso
      
 
