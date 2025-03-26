#suite fibonochi recursif
dico_fibo = {0:1, 1:1}

def fibo_opti(n):
    av_der,der = 0,1
    for i in range(n):
        av_der,der =  der, der+ av_der+der
        
    return der


def fibo(n):
    if n >= len(dico_fibo):
        liste_fibo.append(fibo(n-1)+fibo(n-2))
    return dico_fibo[n]
    


def fibo_pas_opti(n):
    if n <= 1:
        return 1
    
    return fibo(n-1) +fibo(n-2)

liste_piece = [200,100,50,20,10,5,2,1]
def rend_monnaie(montant):
    rendu = []
    if montant > 0:
     
     while liste_piece
                 if i <= montant:
                dico_rendu = rendu_monnaie(montant-piece)
                dico_rendu[piece] += 1
    
    return dico_rendu
    
 