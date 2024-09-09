txt = bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")

for key in range(128):  
    decrypted = bytes([byte ^ key for byte in txt])  
    if "crypto{" in decrypted.decode():
        print(f"Key: {key}, Decrypted text: {decrypted.decode()}")
