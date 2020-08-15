import multiprocessing
class red():
    def __init__(self, x, y, valor):
        self.x = x
        self.y = y
        self.valor = valor
    def __str__(self):
        return f'X : {self.x} Y : {self.y}  Pescados : {self.valor} \n'
def recorrer(lago, inicio, queue,largo, ancho):
    conjunto = []
    print(inicio)
    for j in range(len(lago[1])):
        for i in range(inicio,len(lago),largo):
            suma =0 
        if largo+i <= len(lago):
            if ancho+j <= len(lago[0]):
                for l in range(i, largo+i):
                    for k in range(j,ancho+j):
                        suma+= lago[l][k]
                queue.put(red(j,i, suma))
if __name__ == "__main__":
    Lago = open("Lago.txt")
    lago = [[float(j) for j in i.split(",") ] for i in Lago.readlines()]
    ancho = 2
    largo = 3
    procesos = 4
    queue = multiprocessing.Queue()
    procesos = [multiprocessing.Process(target = recorrer, args= (lago,i, queue, largo, ancho)) for i in range(procesos)]
    [hilo.start() for hilo in procesos]
    [hilo.join() for hilo in procesos]
    resultados = []
    while not queue.empty():
            resultados.append(queue.get())
    for i in resultados:
        print(i)