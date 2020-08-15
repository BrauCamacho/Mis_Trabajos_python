n = int(input('n: '))
x = float(input('x: '))


suma = 0

for k in range(n+1):
    fact = 1
    
    for i in range(1, 2 * k + 1):
        fact *= i
    valor = (1**k)
    valor2 = x **(2 * k)
    suma += valor * (valor2/fact)
    #suma += (a ** k) * ((x**(b*k))/fact)
print(f"resultado: {(suma):.4f}")