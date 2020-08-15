k = int(input())
pi = 2
for i in range(1,k+1):
    pi*=((2*i)**2) / ((2*i-1)*(2*i+1))
print(pi)