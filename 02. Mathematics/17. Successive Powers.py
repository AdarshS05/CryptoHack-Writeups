powers= [588, 665, 216, 113, 642, 4, 836, 114, 851, 492, 819, 237]

for p in range (851,1000):
    for j in range (100,250):
        if ((p**j)%p) == 588:
            print(p,j)
            break
            