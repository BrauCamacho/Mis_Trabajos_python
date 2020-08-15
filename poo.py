class Prueba:
    def __init__(self):
        self.Mensaje = "Hola"
        self.__Mensaje2 = "Privado"
        
    def __str__(self):
        return f'Mensaje = {self.Mensaje}'
if __name__ == "__main__":
    prueba = Prueba()
    print(prueba)
    print(prueba.__dict__)
    print(prueba.Mensaje)
    prueba.Mensaje = "Nuevo"
    print(prueba._Prueba__Mensaje2)
    #print(prueba)
    lista = []
    lista.append(Prueba())
    lista.append(Prueba())
    print(lista[0].Mensaje)