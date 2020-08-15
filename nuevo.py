def fivonacci(cant):
    a =0
    b= 1
    cont =0
    while cont< cant:
        yield a
        a, b =b, a+b
        cont+= 1
def renge(lb, ub=None, step=1):
    if ub is None:
        limit = lb
        cont =0
    else:
        limit = ub
        cont = lb
    while cont < limit:
        yield cont
        cont += step

if __name__ == "__main__":
    for i in fivonacci(10):
         print(i, end=" ")
    for i in renge(5,10,2):
        print(i)
