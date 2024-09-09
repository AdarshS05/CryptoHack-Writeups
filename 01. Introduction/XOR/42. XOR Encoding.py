from pwn import xor

txt = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")
s = "crypto{"

a = []
b = []
i = 0

while i < 7:
    a.append(xor(txt[i], ord(s[i])))
    i += 1

a.append('y')

for j in range(0, len(txt)):
    b.append(xor(txt[j], a[j % 8]))

for byte in b:
    print(byte.decode(), end='') 

print()  
