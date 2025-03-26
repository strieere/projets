def plus_court_chemin(graphe,s,t):
    courant = [s]
    suivant = []
    parcours = {:s[] for s on graphe.adj}
    parcours[s] = [s]
    while courant != []
        c = courant.pop()
        for v in graphe.voisins(c):
            if parcours[v] == []:
                suivant.append(v)
                parcours[v] = parcours[c]+[v]
            
        
        if courant == [] :
            courant, suivant = suivant, courant
    
    return parcours[t]