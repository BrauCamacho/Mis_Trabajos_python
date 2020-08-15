class Saludar:
    def __init__(self, Nombre = None):
        self.Mensaje = "Hola" if Nombre is None else  f'Hola {Nombre}'
    def __str__(self):
        return f'Mensaje = {self.Mensaje}'
    def cambiar_saludo(self, Nombre):
        self.Mensaje = f'Hola {Nombre}'
if __name__ == "__main__":
    #saludar_Juan = Saludar()
    #saludar_Pedro = Saludar('Pedro')
    #saludar_Juan.cambiar_saludo('juan')
    #print(saludar_Juan)
    #print(saludar_Pedro)
    lista = []
    lista.append(Saludar('Braulio'))
    lista.append(Saludar('Eugenio'))
    lista.append(Saludar('Camacho'))
    lista.append(Saludar('Loya'))
    print("\n".join(str(saludo)for saludo in lista))
    print("-"*30)
    print("\n".join(str(saludo)for saludo in sorted(lista,key = lambda x:x.Mensaje)))