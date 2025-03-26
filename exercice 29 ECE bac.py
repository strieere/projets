def moyenne(notes:list) -> float:
    """
    in -> liste de couples note, coefficient
    out -> la moyenne des notes coefficientées
    """
    
    s = 0
    c = 0
    
    for i in range(len(notes)):
        note = notes[i][0]
        coef = notes[1][1]
        
        s += note*coef
        c += coef
        
    return s/c



def ligne_suivante_pascal(ligne):
    '''Renvoie la ligne suivant ligne du triangle de Pascal'''
    ligne_suiv = [1]
    for i in range(1,len(ligne)):
        ligne_suiv.append(ligne[i-1]+ligne[i+1])
        ligne_suiv.append(1)
    return ligne_suiv


def pascal(n):
    '''Renvoie le triangle de Pascal de hauteur n'''
    triangle = [ [1] ]
    
    for k in range(n):
        ligne_k = ligne_suivante_pascal(triangle[k])
        triangle.append(ligne_k)
    return triangle
