n = int(input("Ingrese el número de filas para la pirámide: "))
for i in range(1, n + 1):
    # Imprimir espacios en blanco
    for j in range(0,n-i):
        print(" ", end="")
        
    # Imprimir números decrecientes
    for j in range(i, 0, -1):
        print(j, end="")
        
    # Imprimir números crecientes a partir de 2
    for j in range(2, i + 1):
        print(j, end="")
        
    # Nueva línea después de cada fila
    print()
