#errores de diseño
#1.- lexicos
#lexemas[unidad minima de escritura de código]
#2.- sintaxis
#3.-semanticos(falta de declaracion de variables)
#errores que no podemos preveer
#try{}catch(Exception ex){} en java
#log de errores
#try:
#    uno =int(input("inserte un numero")) 
#    dos =int(input("inserte un numero"))
#except Exception as err:
#    print("numeros hijoe")
lista1 = [1,2]
lista2 = [1,2,4]
out =[]
out2 =[]
for (a,b) in zip(lista1,lista2):
    out.append(a+b)
print(out)
for i, item in enumerate(lista1):
    out2.append(i)
print(out2)