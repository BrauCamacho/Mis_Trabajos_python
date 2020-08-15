import threading, queue

def pi():
    pass#aqui va tu funcion
if __name__=="__main__":
    lista = []
    nH = int(input("numero de hilos"))
    n = int(input("valor a aplicar"))
    for i in nH:
        lista.append(threading.Thread(target = pi, args = (nH, n)))