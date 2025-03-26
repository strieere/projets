class ARBR():
    
    def __init__(self,valeur):
        self.val = valeur
        self.g = None
        self.d = None
        
    
    def inserer(self, nouveau):
        if nouveau > self.val:
            if self.d is None:
                self.d = ARBR(nouveau)
            
            else: self.d.inserer(nouveau)
            
            
        else :
            if self.g is None:
                self.g = ARBR(nouveau)
                
            else: self.g.inserer(nouveau)
            
    
    def rechercher(self,valeur):
        if valeur == self.val:
            return True
        elif valeur > self.val:
            
            if self.d is None :
                return False
            
            return self.d.rechercher(valeur)
        
        else :
            if self.g is None :
                return False
            return self.g.rechercher(valeur)
            
        
            
