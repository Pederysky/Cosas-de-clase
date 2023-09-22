#Realiza un programa que introduciéndole los Kilómetros/Hora me calcule los Metros/Segundo.

velocidad = int(input("Introduce una velocidad en km/h: "))
operacion = (velocidad*1000) / 3600

print("La velocidad es:" , str(operacion),  "m/s")
       