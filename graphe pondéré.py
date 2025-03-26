class graphe_pondere :
    
    def __init__(self, liste_sommets):
        self.s_liste = liste_sommets
        self.n = len(liste_sommets)
        self.mat = [[None]*n for _ in range(n)]
        
    def arc(self,s1,s2,poids):
        i1 = self.s_liste.index(s1)
        i2 = self.s_liste.index(s2)
        self.mat[i1][i2] = poids
        
    
    def voisins(self,s):
        i = self.s_liste.index(s)
        
        return [(self.s_liste[j], self.mat[i][j])
                for j in range(self.n)
                if self.mat[i][j] is not None]
    def poid(self,s1,s2):
        i1 = self.s_liste.index(s1)
        i2 = self.s_liste.index(s2)
        
    
    def djikstra(self,graphe,s1,s2):
        
        

        
    
G = graphe_pondere(['a','b','c','d','e','f','g'])