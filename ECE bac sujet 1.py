def recherche(lettre: str, mot: str) -> int:
    compte = 0
    for i in mot:
        if lettre == i:
            compte += 1
    return compte

lettre = "o"
mot = 'bonjour'

#print(f"la lettre {lettre} s'est répété {recherche(lettre,mot)} dans le mot {mot}")


pieces = [100,50,20,10,5,2,1]

def rendu_glouton(arendre, solution=[],i=0):
    if arendre ==0:
        return solution
    p = pieces[i]
    if p <= arendre:
        solution.append(p)
        return rendu_glouton(arendre-p,solution,i)
    else:
        return rendu_glouton(arendre,solution,i+1)

print(rendu_glouton(68,[],0))