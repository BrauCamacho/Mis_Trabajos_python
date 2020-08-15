import multiprocessing
# el programa calcula pi como ya habiamos visto antes, solo que toma el proceso grande y lo divide en subrpocesos para que se ejecuten de manera paralela y reducir el tiempo de ejecucion
#re100 servidito bb
def cal_pi(li, ls, step, queue):
    pi =1
    for k in range(li, ls+1, step):
        val = 2*k
        pi*=(val**2)/((val-1)*(val+1))
    queue.put(pi)

if __name__ == "__main__":
    n = input()
    hi =input()
    n= int(n)
    hi = int(hi)
    queue = multiprocessing.Queue()
    procesos = [multiprocessing.Process(target = cal_pi, args= (i,n, hi, queue)) for i in range(1,hi+1)]
    [proceso.start() for proceso in procesos]
    [proceso.join() for proceso in procesos]
    pi =2
    while not queue.empty():
        pi*= queue.get() 
    print(pi)
        