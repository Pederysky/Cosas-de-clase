from random import randint

#Función lanzar dado
def lanzar_dado():
    return randint(1,6)

print("Bienvenidos a LANZANDO DOS DADOS")
p1 = 0
p2 = 0
decision1 = 's'
decision2 = 's'
t1 = 0
t2 = 0

while (p1 < 21 and decision1 !='n' ) or (p2 < 21 and decision2 !='n' ):
#Tirada Jugador 1
    if decision1 != 'n' and p1 < 21:
        input("Jugador 1 presiona cualquier tecla para lanzar ")
        dado1=lanzar_dado()
        p1+=dado1
        t1+=1
        print(f"El Jugador 1 ha sacado {dado1}")
        print(f"Tirada actual: {t1}")
        print(f"Puntuación Total: {p1}")
        if p1 > 21:
            break
        elif p1 < 21:
            decision1=input("Si quieres dejar de lanzar pulsa 'n' ").lower()
    

#Tirada jugador 2
    if decision2 != 'n' and p2 < 21:
        input("Jugador 2 presiona cualquier tecla para lanzar ")
        dado2=lanzar_dado()
        p2+=dado2
        t2+=1
        print(f"El Jugador 2 ha sacado {dado2}")
        print(f"Tirada actual: {t2}")
        print(f"Puntuación Total: {p2}")
        if p2 > 21:
            break
        elif p2 < 21:
            decision2=input("Si quieres dejar de lanzar pulsa 'n' ").lower()


#Resultado
if (p1 > p2) and (p1 <=21) or p2 > 21:
    print(f"Ha ganado el Jugador 1 con {p1} puntos. Tiradas totales:{t1}")
elif (p1 < p2) and (p2 <=21) or p1 > 21:
    print(f"Ha ganado el Jugador 2 con {p2} puntos. Tiradas totales:{t2}")
elif (p1 > 21) and (p1 > 21):
    print(f"Ambos Jugadores pierden. El Jugador 1 ha obtenido {p1} puntos con {t1} tiradas y el Jugador 2 ha obtenido {p2} puntos con {t2} tiradas")
else:
    print(f"¡Empate! El Jugador 1 ha obtenido {p1} puntos con {t1} tiradas y el Jugador 2 ha obtenido {p2} puntos con {t2} tiradas")