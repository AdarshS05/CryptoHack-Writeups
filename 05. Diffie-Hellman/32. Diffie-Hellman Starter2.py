p = 28151 

factors = [i for i in range (1,p) if ((p-1)%i == 0)]     
print(factors)
m= factors[-2]

for j in range (1,p):
    if ((j**m)%p != 1):
        print(j)
        break
        
        