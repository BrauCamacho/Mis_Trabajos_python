lista =[]
lista.append({"INE":1, "Nombre":"pedro"})
lista.append({"INE":5, "Nombre":"braulio"})
lista.append({"INE":4, "Nombre":"juan"})
lista.append({"INE":2, "Nombre":"carlos"})
#ordenamiento asignando una nueva lista
lista2 = sorted(lista, key = lambda x:x["Nombre"])
#ordenamiento sobre la misma lista
lista.sort(key = lambda x:x["INE"])
print("-"*30)
print(lista)
print("-"*30)
print(lista2)
