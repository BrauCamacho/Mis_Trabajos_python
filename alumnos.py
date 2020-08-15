lista = []
dec = 1
while dec != 0:
    dec = int(input("1 para capturar y 0 para salir"))
    if dec == 1:
        salon = {}
        salon["Grupo"] = int(input("introduce el numero de grupo"))
        salon["Alumnos"] = int(input("introduce el numero de alumnos"))
        salon["Promedio"] = float(input("introducir el promedio de el salon"))
        lista.append(salon)
    else:
        print("saliendo...")
lista_numalum = sorted(lista, key = lambda x:x["Alumnos"])
lista_promedio = sorted(lista, key = lambda x:x["Promedio"])
print(f"menor numero de alumnos: {lista_numalum[0]}")
print(f"mayor numero de alumnos: {lista_numalum[len(lista_numalum)-1]}")
print(f"menor promedio de alumnos: {lista_promedio[0]}")
print(f"menor promedio de alumnos: {lista_promedio[len(lista_numalum)-1]}")

     