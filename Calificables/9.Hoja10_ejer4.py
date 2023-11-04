#Función para calcular la duración total en segundos
def calcular_segundos(horas, minutos, segundos):
    return horas * 3600 + minutos * 60 + segundos

#Función para transformar segundos a horas, minutos y segundos
def transforma_a_horas(total_segundos):
    horas = total_segundos // 3600
    minutos = (total_segundos % 3600) // 60
    segundos = total_segundos % 60
    return (f"{horas}h {minutos}m {segundos}s")

#Función para calcular el coste de una comunicación en céntimos
def calcular_coste(segundos, tarifa):
    coste = segundos * tarifa
    return coste

#Función para convertir céntimos a euros y céntimos
def centimos_a_euro(total_centimos):
    euros = total_centimos // 100
    centimos = round(total_centimos % 100, 2)
    return (f"{euros}€ {centimos}cent")

#Pedimos los datos
tarifa_por_segundo = float(input("Introduce la tarifa por segundo (en euros): "))
num_comunicaciones = int(input("Introduce el número de comunicaciones realizadas: "))


tiempo_total_segundos = 0
coste_total_centimos = 0


for i in range(num_comunicaciones):
    print(f"Comunicación {i+1}:")
    horas = int(input("Horas: "))
    minutos = int(input("Minutos: "))
    segundos = int(input("Segundos: "))
    
    #Calcular la duración en segundos
    duracion_segundos = calcular_segundos(horas, minutos, segundos)
    
    #Calcular el coste en céntimos
    coste_comunicacion = calcular_coste(duracion_segundos, tarifa_por_segundo)
    
    tiempo_total_segundos += duracion_segundos
    coste_total_centimos += coste_comunicacion
    
    print(f"Duración: {transforma_a_horas(duracion_segundos)}")
    print(f"Coste de la comunicación: {centimos_a_euro(coste_comunicacion)}")


print("Factura:")
print(f"Tiempo total consumido: {transforma_a_horas(tiempo_total_segundos)}")
print(f"Coste total: {centimos_a_euro(coste_total_centimos)}")
