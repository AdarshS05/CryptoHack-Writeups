def inner_product(v1, v2):
    s = 0
    for i in range(len(v1)):
        s = s + v1[i] * v2[i]
    return s

def size(v):
    s = 0
    for i in range(len(v)):
        s = s + v[i] ** 2
    return s ** 0.5


v = [846835985, 9834798552]
u = [87502093, 123094980]
temp= []

while True:
    if (size(v)>size(u)):
        temp=v
        v=u
        u=temp

    m= round(inner_product(v,u)/inner_product(v,v))
    if m==0:
        print(inner_product(v,u))
        break
    for k in range(len(v)):
        u[k]=u[k]-m*v[k]