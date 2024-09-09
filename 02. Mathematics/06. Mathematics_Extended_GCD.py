def gcd(a,b):
    if (a==0):
        return b,0,1
    else:
        p,q,r= gcd(b%a,a)
        s=r-(b//a)*q
        t=q
        return p,s,t
    
a,b,c= gcd(26513,32321)
print(a,b,c)
