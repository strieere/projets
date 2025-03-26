def insertion_arbre(a,cle):
    (g, v, d) = a
    arbr = a
    g = None
    d = None
    if a == None:
        return False
    
    if g == None:
        g.append(cle)
    
    elif cle > g :
        if cle == None:
            d.append(cle)
        else:
            if cle > d:
                insertion_arbre(a,cle)
            



n0 = (None, 0, None)
n3 = (None, 3, None)
n2 = (None, 2, n3)
abr1 = (n0, 1, n2)
