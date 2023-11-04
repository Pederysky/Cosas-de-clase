class Ejemplo: 
    def publico(self): 
        print("Publico")
        self.__privado()
    def __privado(self): 
        print("Privado")

ej = Ejemplo()
ej.publico()
#ej.__privado()

print (dir (ej))
print ("")