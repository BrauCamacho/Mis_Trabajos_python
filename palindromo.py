valor = input("introducir un palindrom").lower().replace(" ", "")
print("el string es un palindromo") if valor == valor[::-1] else print("no es un palindromo") 
#in - programa que cuente cuantas vocales hay en una frase
cont= 0
for i in range(len(valor)):
   cont+=1 if valor[i] in "aeiou" else 0
print(cont)
cont = sum([1 if letra in "aeiou" else 0 for letra in valor])
print(cont)
