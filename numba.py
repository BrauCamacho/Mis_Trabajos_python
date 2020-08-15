import random
import time
import numpy as np
dim =10
lista1 = [random.random() for i in range(10)]
lista2 = [random.random() for i in range(10)]
#incorrecta

lista3 = []
for i in range (dim):
    lista3.append(lista1[i]+ lista2[i])

#mas o menos
lista4 = []
for (x,y) in zip(lista1, lista2):
    lista3.append(x+y)
#correcta
lista5 = [ x+y for (x,y) in zip(lista1, lista2)]
#numpy
lista1_np = np.array(lista1)
lista2_np = np.array(lista2)
lista5 = lista1_np+lista2_np
print(lista5)