def gcd(a,b):
    if (a==0):
        return b
    else:
        return (gcd(b%a,a))
    
x= int(input())
y= int(input())
print(gcd(x,y))