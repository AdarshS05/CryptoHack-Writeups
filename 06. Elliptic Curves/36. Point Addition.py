k=7
a=3
P = [493, 5564]
Q = [1539, 4742]
R = [4403,5202]

def add(x, y):  
    z = [0, 0]
    if x != y:
        l = ((y[1] - x[1]) * pow(y[0] - x[0], -1, k)) % k
    else:
        l = ((3 * pow(x[0], 2) + a) * pow(2 * x[1], -1, k)) % k

    z[0] = (pow(l, 2) - x[0] - y[0]) % k
    z[1] = (l * (x[0] - z[0]) - x[1]) % k
    return z


b= add(P,P)
#print(b)
c= add(Q,R)

print(add([0,3],[0,3]))



