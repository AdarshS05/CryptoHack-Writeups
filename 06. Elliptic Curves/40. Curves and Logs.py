from hashlib import sha1
from Crypto.Util.number import *


k = 9739
a=497
P = [1804,5368]
Qa= [815, 3190]
n=1829

def point_add(P, Q):
    if P == [0, 0]:
        return Q
    if Q == [0, 0]:
        return P
    if P[0] == Q[0] and (P[1] != Q[1] or P[1] == 0):
        return [0, 0]
    if P != Q:
        lam = ((Q[1] - P[1]) * pow(Q[0] - P[0], -1, k)) % k
    else:
        lam = ((3 * P[0] ** 2 + a) * pow(2 * P[1], -1, k)) % k
    Rx = (lam ** 2 - P[0] - Q[0]) % k
    Ry = (lam * (P[0] - Rx) - P[1]) % k
    return [Rx, Ry]

def point_double(P):
    lam = ((3 * P[0] ** 2 + a) * pow(2 * P[1], -1, k)) % k
    Rx = (lam ** 2 - 2 * P[0]) % k
    Ry = (lam * (P[0] - Rx) - P[1]) % k
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

S= scalar_multiply(Qa,n)
print(S)
enc= (sha1(str(S[0]).encode('utf-8')).hexdigest())

print(enc)
