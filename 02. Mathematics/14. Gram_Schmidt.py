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


u = [[4, 1, 3, -1], [2, 1, -3, 4], [1, 0, -2, 7], [6, 2, 9, -5]]
v = [[], [], [], []]

v[0] = u[0]

for i in range(1, len(v)):
    for j in range(1,len(v) - 1):
        m = inner_product(v[j], u[i]) / (size(v[j]) ** 2)
        for k in range(len(v[i])):
            v[k]=m*v[k]
        print(v)
        #v[i] = u[i] - v[j]

print(v)

