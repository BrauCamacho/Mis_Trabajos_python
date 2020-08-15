import math, random
from scipy.stats import norm
def verificar(v, minvar):
    ret = 0
    for i in v:
        if i > minvar:
            ret +=1
    return ret
def prod(vector):
    val = 1;
    for i in vector:
        val*=i
    return val
def truncar(fitness, poblacion, turn):
    for i in fitness:
        for j in range(len(fitness)-1):
            if fitness[j] > fitness[j+1]:
                aux = fitness[j]
                auxi = poblacion[j]
                fitness[j] = fitness[j+1]
                poblacion[j] = poblacion[j+1]
                fitness[j+1] = aux
                poblacion[j+1] = auxi
    return [poblacion[i] for i in range(turn)]

class funcion:
    def __init__(self):
        self.rango = None
        self.funcion = None
    def spthere(self):
        self.rango = (-5.12,5.12)
        self.funcion = "sum([(x**2) for x in vector])"
    def ackley(self):
        self.rango = (-32.768,32.768)
        self.funcion = "-20*math.exp(-0.2*math.sqrt(sum([(x**2) for x in vector])/(len(vector)))) - math.exp(sum([math.cos(2*math.pi*x) for x in vector])) + 20 + math.exp(1)"
    def griewank(self):
        self.rango = (-600, 600)
        self.funcion = "sum([(x**2)/4000 for x in vector]) - prod([math.cos(x/math.sqrt(1)) for x in vector]) +1"
if __name__ == "__main__":
   ind = 100
   dim = 10 
   trunc = 10
   minvar = 0.5
   funcion = funcion()
   funcion.spthere()
   Poblacion = [[random.uniform(funcion.rango[0],funcion.rango[1]) for x in range(dim)]for x in range(ind)]
   verif = -1
   while verif != 0:
    fitness = [(eval(funcion.funcion)) for vector in Poblacion] 
    truncada = truncar(fitness, Poblacion, trunc)
    vector = truncada[0]
    mejor = eval(funcion.funcion)
    #print(mejor)
    gtestada = [eval(funcion.funcion)- mejor +1 for vector in truncada]
    #print(gtestada)
    medias = []
    for i in range(dim):
       divisor = sum([truncada[j][i]*gtestada[j] for j in range(len(truncada))])
       dividendo = sum([gtestada[j] for j in range(len(truncada))])
       medias.append(divisor/dividendo)
    v = []
    for i in range(dim):
       divisor = sum([gtestada[j]*((truncada[j][i]-medias[i])**2) for j in range(len(truncada))])
       dividendo = sum([gtestada[j] for j in range(len(truncada))])
       v.append(divisor/(dividendo+1))
    for i in range(dim):
        for j in range(ind):
            Poblacion[j][i] = round(random.gauss(medias[i], math.sqrt(v[i])))
    v = [round(i,1) for i in v]
    medias = [round(i,1) for i in medias]
    verif = verificar(v, minvar)
    print("Medias")
    print(v)
    print("desviaciones estandar")
    print(medias)
print("Mejor individuo :")
print(truncar(fitness, Poblacion, trunc)[0])
   
   