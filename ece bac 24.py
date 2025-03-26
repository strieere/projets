liste = [1.0, 2.0, 4.0]

def moyenne(lst:list) -> float :
    nb = 0
    for i in range(len(lst)):
        nb += lst[i]
    return nb/len(lst)





def binaire(a):
    '''convertit un nombre entier a en sa representation 
    binaire sous forme de chaine de caractères.'''
    if a == 0:
        return '0'
    bin_a = ""
    while a > 0 : 
        bin_a = str(a%2) + bin_a 
        a = a//2
        print(a)
    return bin_a


print(binaire(314))