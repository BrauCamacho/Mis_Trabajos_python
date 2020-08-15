import math, random
class Lugares:
    def __init__(self,latitud, longitud, descripcion):
        self.latitud = latitud
        self.longitud = longitud
        self.descripcion = descripcion
    def __str__(self):
        return f'Latitud: {self.latitud} \nLongitud: {self.longitud} \n Descripcion: {self.descripcion}'
    def __add__(self, other):
        return math.sqrt(((self.latitud-other.latitud)**2)+((self.longitud-other.longitud)**2))
class Distancias:
    def __init__(self, Distancia, Lugar):
        self.distancia = Distancia
        self.Lugar = Lugar
    def __str__(self):
        return f'Distancia con respecto de el lugar de referencia: {self.distancia} \n {self.Lugar}'
if __name__ =="__main__":
    ListaDeLugares = []
    cont =0
    with open("atractores.txt", "r") as fp:
        for line in fp.readlines():
            if cont != 0:
                linea = line.split(",")
                lugar = Lugares(float(linea[0]), float(linea[1]), linea[2])
                ListaDeLugares.append(lugar)
            cont+=1
    ListaDeDistancias = []
    dec = random.randint(0, len(ListaDeLugares)-1)
    print(f"Lugar de referencia: \n{ListaDeLugares[dec]}")
    for i in ListaDeLugares:
        distancia = Distancias((ListaDeLugares[dec]+i),i)
        ListaDeDistancias.append(distancia)
    lista_ordenada = sorted(ListaDeDistancias,key = lambda x:x.distancia)
    for i in lista_ordenada:
        print(i)


    
