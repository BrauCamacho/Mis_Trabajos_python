n = float(input("n "))
X = float(input("X "))
resp=0
for i in range(int(n)):
    fact = 1
    f = (i)
    for l in range(1,f+1):
        fact*=l
    resp+=(X**i)/fact
print(resp)