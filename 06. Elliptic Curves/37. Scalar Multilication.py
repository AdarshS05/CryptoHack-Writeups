k = 9739
n = 7863
P = [2339, 2213]

def point_add(P, Q):
    a = 497
    p = 9739
    if P == [0, 0]:
        return Q
    if Q == [0, 0]:
        return P
    if P[0] == Q[0] and (P[1] != Q[1] or P[1] == 0):
        return [0, 0]
    if P != Q:
        lam = ((Q[1] - P[1]) * pow(Q[0] - P[0], -1, p)) % p
    else:
        lam = ((3 * P[0] ** 2 + a) * pow(2 * P[1], -1, p)) % p
    Rx = (lam ** 2 - P[0] - Q[0]) % p
    Ry = (lam * (P[0] - Rx) - P[1]) % p
    return [Rx, Ry]

def point_double(P):
    a = 497
    p = 9739
    lam = ((3 * P[0] ** 2 + a) * pow(2 * P[1], -1, p)) % p
    Rx = (lam ** 2 - 2 * P[0]) % p
    Ry = (lam * (P[0] - Rx) - P[1]) % p
    return [Rx, Ry]

def scalar_multiply(P, n):
    Q = P
    R = [0, 0]
    while n > 0:
        if n & 1:
            R = point_add(R, Q)
        Q = point_double(Q)
        n >>= 1
    return R

b = scalar_multiply(P, n)
print(b)
