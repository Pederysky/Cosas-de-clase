while True:
    print("/***MENÚ. HAY HAMBRE***/")
    print("a) Quiero Arroz con pollo")
    print("b) Quiero pizza")
    print("c) Quiero sopa")
    print("d) Quiero unas cocretas")
    print("e) Salir")
    opcion = input("Elige una opción ").lower()

    if opcion == "a":
        print ("Está Bueenaaaaaardo")
    elif opcion == "b":
        print ("Pero no para cenar")
    elif opcion == "c":
        print ("Pero no para cenar")
    elif opcion == "d":
        print ("Acompañadas de una cervecita booohhhh")
    elif opcion == "e":
        print ("SALIR")
        break
    else:
        print("Opcion no valida. Te quedas con Hambre.")