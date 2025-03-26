class Arbre:
    
    def __init__(self,valeur,enfants = None):
        self.val = valeur
        if enfants is None :
            self.enf = []
        self.enf = enfants
        
    
    def est_feuille(self):
        return self.enf == []
        
        
        
    def hauteur(self):
        h = 0
        
        for e in self.enf:
            if e.hauteur > h:
                h += e.hauteur()
                
        return h+1
        
        
    def taille(self):
        t = 1
        for i in self.enf:
            t += e.taille()
        
        return t
        
        
        
        

F = Arbre('F', [])
C = Arbre('C', [])
D = Arbre('D', [])
B = Arbre('B', [C, D])
C1 = Arbre('C', [F])
A = Arbre('A', [B, C1])
