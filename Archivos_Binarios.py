import pickle
if __name__ == "__main__":
    #lis = []
    lista = ["Pedro", 20, "Juan", 5.5, 3+4]
    with open("Datos.txt", "wb") as fp:
        pickle.dump([lista,lista], fp)
        
    with open("Datos.txt", "rb") as fp:
        lista2  = pickle.load(fp)
        print(lista2)
          