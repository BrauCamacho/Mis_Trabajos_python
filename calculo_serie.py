x = float(input())
n = int(input())
resp =0
for i in range(n+1):
    fact = 1
    for l in range(1,2*i+1):
        fact*=l
    valor = (-1)**i
    valor2 = x**(2*i)
    resp+= valor*(valor2/fact)
print(resp)