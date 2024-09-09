def inner_product(v1,v2,m,n):
    s=0
    for i in range(len(v1)):
        s=s+m*v1[i]*n*v2[i]
    print(s)


v=[2,6,3]
w=[1,0,0]
u=[7,7,2]

for i in range(len(v)):
    v[i]=2*v[i]-w[i]
inner_product(v,u,3,2)