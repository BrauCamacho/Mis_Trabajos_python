import random
d = float(input("Dimensiones: "))
n = float(input("Learning rate: "))
Probabilidades = [ 0.5 for x in range(int(d))]
mejor =-1
while(mejor < d): 
    Ind1 = [1 if(x > random.random()) else 0 for x in Probabilidades ]
    IndSuma1 = sum(Ind1) 
    Ind2 = [1 if(x > random.random()) else 0 for x in Probabilidades ] 
    IndSuma2 = sum(Ind2)
    mej = Ind1 if(IndSuma1 > IndSuma2) else Ind2
    men = Ind1 if(IndSuma1 < IndSuma2) else Ind2
    Probabilidades = [Probabilidades[i] if (men[i] == mej[i]) else  Probabilidades[i]+(1/n) if (mej[i] == 1 and Probabilidades[i] < 1)else Probabilidades[i]-(1/n) if (mej[i] == 0 and Probabilidades[i] > 0) else Probabilidades[i] for i in range(len(Probabilidades))]
    Probabilidades = [round(x,2) for x in Probabilidades]
    mejor = sum(Probabilidades)
    print(Probabilidades)