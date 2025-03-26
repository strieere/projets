class Arbre_binaire:
    
    def __init__(self, valeur, gauche = None, droit = None):
        self.val = valeur
        self.g = gauche
        self.d = droit
        
        
    def ajouter_gauche(self, arbre):
        self.g = arbre
        
    
    def ajouter_droit(self,arbre):
        self.d = arbre
        
    
    def taille(self):
        t = 1
        
        if self.g != None :
            t += self.g.taille()      
        if self.d != None :
            t += self.d.taille()
    
        return t
    
        
    def hauteur(self):
        h = 0
        if self.g:
            h = self.g.hauteur()  # Calcul de la hauteur du sous-arbre gauche
        if self.d:
            h = max(h, self.d.hauteur())  # Comparer et prendre la plus grande hauteur
        return h + 1  # Ajouter 1 pour le nœud actuel
    
    
    def prefixe(self):
        L  = [self.val]
        
        if self.g :
            L += self.g.prefixe()   
        if self.d :
            L += self.d.prefixe()
        
        return L
  
  
    def suffixe(self):
        L = []
        
        if self.g :
            L += self.g.suffixe()
        if self.d:
            L += self.d.suffixe()
        
        L.append(self.val)
        return L
    
    
    def largeur(self):
        courant = [self]
        suivant = []
        parcour = []
        
        while courant :
            c = courant.pop
            parcour.append(c.val)
            
            if c.g :
                suivant.append(self.g)
            if c.d :
                suivant.append(self.d)
            if courant == []:
                courant,suivant = suivant, []
            
        return parcour
    
#file = parcour en largeur non recursif
#pile = parcour en profondeur non récursif



F = Arbre_binaire('F')
E = Arbre_binaire('E', F)
G = Arbre_binaire('G')
D = Arbre_binaire('D', None, G)
C = Arbre_binaire('C')
B = Arbre_binaire('B', C, D)
A = Arbre_binaire('A', B, E)


            
            
            