#este es mi regalo de navidad(no tengo dinero jeje perdón), te quiero mucho, mas de lo que crees, que tengas una feliz navidad
import math,random
def generaralfa(len):
    alfa = []
    for i in range(len):
        alfa.append(random.random())
    return alfa
def generar(ionos, sel):
    datos = []
    uno =0
    cero =0
    for l in ionos.readlines():
        Linea = {}
        Li = l.split(",")
        if Li[34] == "g\n" and uno < sel:
            Linea["Clase"] = 1
            uno+=1
            Linea["Arreglo"] = [float(Li[i]) for i in range(len(Li)-1)]
            datos.append(Linea)
        elif Li[34] == "b\n" and cero < sel:
            Linea["Clase"] = 0
            cero+=1
            Linea["Arreglo"] = [float(Li[i]) for i in range(len(Li)-1)]
            datos.append(Linea)
    return datos
    def proceso(conj):
        miu = 1
        eps = 0.01
        delt = 0.05
        alfa = generaralfa(34)
        for epoca in range(1,1001):
            niu = 1/(4*math.sqrt(epoca))
            for i in datos:
                sim = math.sqrt(sum([j**2 for j in alfa]))
                alfa = [j/sim for j in alfa]
                sumatoria = sum([i["Arreglo"][j]*alfa[j] for j in range(len(i["Arreglo"]))])
                obtenido = 1 if sumatoria >=0 else -1
                if obtenido > i["Clase"]+eps and sumatoria >=0:
                arreglo = [ for j in i["Arreglo"]]
                elif obtenido < i["Clase"]-eps and sumaroria < 0:
                z = Vector.vector
                elif obtenido <= i["Clase"]+eps and sumatoria >=0 and sumatoria < delt:
                z = m*Vector.vector
                elif obtenido >= i["Clase"]-eps and sumatoria >=(delt*-1) and sumatoria < 0:
                z = m*(Vector.vector*(-1))
                else :
                z = 0
                Pesos = Pesos+n*z
  
if __name__ =="__main__":
    ionos = open("ionosphere.data","r")
    conj = generar(ionos,5)# ionos, son todos los datos, y el 5 es el numero que 
