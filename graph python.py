class Graphe:

    def __init__ (self, adj = None) :
        if adj is None:
         self.adj = {}
         
        else: self.adj = adj


    def arc (self, s1, s2):
        return s2 in self.adj[s1]


    def sommets (self):
        return list(self.adj)


    def voisins (self, s):
        return self.adj[s]
    
    def parcours_profondeur_rec(graphe : Graphe, depart : str) -> list :
        parcour = []
        
        
        def explorer(sommet):
            if sommet in parcour :
                return parcour
            
            parcour.append(sommet)
            
            for v in graphe.voisins(sommet) :
                explorer(v)
            return parcour
        
        return explorer(depart)
    
    
    def existe_chemin(graphe,s,t):
        #return t in parcours_profondeur_rec(graphe, s)
        
        for v in parcours_profondeur(graphe,s):
            if t == v :
                return True
        
        return False
    
    def parcour_profondeur(graphe : Graph, depart : str):
        # depart est le sommet
        parcour = []
        pile = [depart]
        
        while pile != [] :
            
            explore = pile.pop()
            
            if explore not in parcour:
                parcour.append(explore)
            
            for v in groupe.voisins(explore):
                pile.append(v)
                
        return parcour
    
    def existe_cycle(graphe):
        # pas à apprendre
        vu = []
        
        if s not in vu :
            pile = [()]
            
        while pile != []:
            explore,parent = pile.pop()
            if explore not in vu :
                vu.append(explore)
                
                for v in graphe_voisins(explore):
                    if v not in vu :
                        pile.append((v,explore))
                
    
    
    
    
            
            