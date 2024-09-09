def quadratic_residue(p):
    j= []
    ints = [14,6,11]
    for i in range (0,p):
        j.append(i**2%p)

    for k in range (0,p): 
        if j[k] in ints:
            print(k)
quadratic_residue(29)