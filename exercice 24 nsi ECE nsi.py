def insertion_arbr(a,cle):
    if a is None:
        return (None,cle,None)
    gauche, racine, droit = a
    if cle < racine:
        gauche = insertion_arbr(gauche,cle)
    elif cle > racine:
        droit = insertion_arbr(droit,cle)
    return (gauche,racine,droit)
    
n0 = (None,0,None)
n3 = (None,3,None)
n2 = (None,2,None)
arbr1 = (n0,1,n2)

print(insertion_arbr(arbr1,2))
