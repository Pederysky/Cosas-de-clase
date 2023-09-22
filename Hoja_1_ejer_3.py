# #. Realiza un programa que lea una temperatura en grados centígrados y 
# la pase a grados Kelvin, Farenheit, grados cochinillos y grados alubianos.
#     • ºK= ºC + 273
#     • ºF=ºC*2.1 + 55 (Esto es mentira)
#     • ºCochinillos= ºC*22 + 123 – 2 + ºC/ºK;
#     • ºAlubianos= (ºC - ºCochinillos + ºF) / ºK;


temp = int(input("Introduce la temperatura: "))

K = temp + 273
F = (temp * 2.1) + 55
C = (temp * 22) + 123 - 2 + (temp/K)
A = (temp - C + F) / K

print("La temperatura es " + str(K) + "º kelvin")
print("La temperatura es " + str(F) + "º farenheit")
print("La temperatura es " + str(C) + "º cochinillos")
print("La temperatura es " + str(A) + "º alubianos")