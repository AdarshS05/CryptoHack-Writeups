from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from hashlib import sha1
import hashlib

def is_pkcs7_padded(message):
    padding = message[-message[-1]:]
    return all(padding[i] == len(padding) for i in range(0, len(padding)))


def decrypt_flag(shared_secret: int, iv: str, ciphertext: str):
    # Derive AES key from shared secret
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16]
    # Decrypt flag
    ciphertext = bytes.fromhex(ciphertext)
    iv = bytes.fromhex(iv)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)

    if is_pkcs7_padded(plaintext):
        return unpad(plaintext, 16).decode('ascii')
    else:
        return plaintext.decode('ascii')

k = 9739
a= 497
b= 1768
P = [1804,5368]
Qa= [4726]

n= 6534

b=1768
i=4726

for j in range (k):
    if (Qa[0]**3+(a*Qa[0])+b)%k==(j**2)%k:
        Qa.append(j)

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
shared_secret = S[0]
iv = 'cd9da9f1c60925922377ea952afc212c'
ciphertext = 'febcbe3a3414a730b125931dccf912d2239f3e969c4334d95ed0ec86f6449ad8'

print(decrypt_flag(shared_secret, iv, ciphertext))


