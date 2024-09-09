from Crypto.Util.number import *
k1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
k2 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
k3= "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
k = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"

e2= bytes_to_long(bytes.fromhex(k2))
e3= bytes_to_long(bytes.fromhex(k3))
e= bytes_to_long(bytes.fromhex(k))

key1= bytes_to_long(bytes.fromhex(k1))
key2= key1^e2
key3= key1^e2^e3

flag = key1^e2^e3^e

print(long_to_bytes(flag))