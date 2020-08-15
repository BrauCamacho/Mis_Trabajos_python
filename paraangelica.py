import threading,queue 
# el programa calcula pi como ya habiamos visto antes, solo que toma el proceso grande y lo divide en subrpocesos para que se ejecuten de manera paralela y reducir el tiempo de ejecucion
def cal_pi(queue):
    pi =1
    
    queue.put(pi)
    
if __name__ == "__main__":
    n = int(input()) #pidel valor que se va a aplicar a pi
    hi =int(input()) #pide la cantidad de hilos 
    queue = queue.Queue() # permite a los compartir informacion una vez terminado la ejecucion de el programa
    hilos = [] #crea una lista vacia
    for i in range(1,hi+1):#itera la cantidad de hilos que necesites
        hilos.append(threading.Thread(target = cal_pi, args= (queue))) #llena la lista con los hilos
    for hilo in hilos:
        hilo.start()#los inicializa
    for hilo in hilos:
        hilo.join()#los une
    pi =2
    #la clase queue funciona como una pila, es decir que el ultimo objeto en entrar, es el primero en salir
    while not queue.empty():#mientras la pila tenga objetos, sigue iterando
        pi+= queue.get() #obtiene el valor contenido dentro le la pila
    print(pi) #imprime el valor de pi
        