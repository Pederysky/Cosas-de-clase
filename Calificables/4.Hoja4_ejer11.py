num = int(input("Introduce un número: "))
if num <= 1:
    print("Escribe un número entero mayor que 1")
else:

    def primo(num):
        for i in range(2, num):
            if num % i == 0:
               return False
        return True
                
    
    if primo(num):
        print("Es primo")
    else:
        print("No es primo, los divisores son: ")
        for i in range(2,num):
            if num % i == 0:
                print(f"{i}",end=",")
       

    
