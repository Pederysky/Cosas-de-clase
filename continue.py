while True:
    n=int(input("Introduce un Numero:"))


    if n==0:
        print ("Nos salimos")
        break
    elif n<0:
        print ("Numero Negativo")
        continue
    
    
    print (f"N vale {n}")

