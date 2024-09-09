def findx(rem, mod):
    m = 1
    x = 0
    for i in mod:
        m = m * i
    
    n = [m / j for j in mod]
    o = [b for a in range(len(mod)) for b in range(mod[a]) if (n[a]*b % mod[a] ==1)]
    
    for k in range(len(mod)):
        x=x+ n[k]*rem[k]*o[k] 
    print(x%m)

findx([2, 3, 5], [5, 11, 17])
