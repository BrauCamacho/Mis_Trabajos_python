import random
def individuos(Prob):
    Individuo = []
    for i in Prob:
        if i >  random.random():
            Individuo.append(0)
        else:
            Individuo.append(1)
    return Individuo
Prob = []
dim = int(input("dimensiones: "))
n = float(input("N : "))
for i in range(dim):
    Prob.append(0.5)
SumadeProbabilidades =0
while(SumadeProbabilidades < dim):
    Individuo1 = individuos(Prob)
    Individuo2 = individuos(Prob)
    suma1 = sum(Individuo1)
    suma2 = sum(Individuo2)
    if suma1 > suma2:
        mejor = Individuo1
        peor = Individuo2
    else:
        mejor = Individuo2
        peor = Individuo1
    for i in range(dim):
        if mejor[i] == peor[i]:
            Prob[i] = Prob[i]
        elif mejor[i] == 1 and Prob[i] < 1:
            Prob[i]+= 1/n
        elif mejor[i] == 0 and Prob[i] > 0:
            Prob[i]-= 1/n
        else:
            Prob[i] = Prob[i]
    for i in range(dim):
        Prob[i] = round(Prob[i], 3)
    SumadeProbabilidades = sum(Prob)
    print(Prob)
    


