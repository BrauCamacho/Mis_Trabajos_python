lista = []
for i in range(2,21,2):
    lista.append(i)
print(lista)
#lo mismo pero comprimido
lista2= [val for val in range(2,21,2)]
print(lista2)
valor = 0
#if ternario
valor = 10
Edad = 10 if valor < 20 else 0
print (Edad)
#strings
nombre = " Juan "
print(nombre[0:2])
print(nombre[:3])
print(nombre[-1])
print(nombre[::-1])
print(lista[::-1])
#print(nombre.suorted())
print(sorted(nombre))
print(nombre.upper())
print(nombre.lower())

print(nombre.split("a"))
print(nombre.replace("a","A"))
print(nombre.strip())