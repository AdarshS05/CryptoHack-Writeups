def sol(a,b,m):
    for i in range(m):
        if ((a*i-b)%m)== 0:
            return i
        
print(sol(3,1,13))