# Realiza un programa que lea pulgadas y pase a pies, codos, varas, indices, orejas y jamones.
# pies = pulgadas /15	
# codos = pies/1.3		
# varas = codos/1.23
# indices = pulgadas* 0.85	
# orejas = pulgadas* 0.99+ 2	
# jamones = varas – 12 + (indices * orejas)/codos



pulgadas = int(input("Introduce las pulgadas: "))
pies = pulgadas / 15
codos = pies / 1.3
varas = codos / 1.23
indices = pulgadas * 0.85
orejas = (pulgadas * 0.99) + 2
jamones = varas - 12 + ((indices * orejas) / codos)

print("La medida es  " + str(pies) + " pies")
print("La medida es  " + str(codos) + " codos")
print("La medida es  " + str(varas) + " varas")
print("La medida es  " + str(indices) + " indices")
print("La medida es  " + str(orejas) + " orejas")
print("La medida es  " + str(jamones) + " jamones")
