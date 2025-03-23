url = str(input("enter the url: "))


#avoir un dico montrant le code ascii de chaque lettre d'url
def lettre_ascii(url:str) -> dict:
    lettre_bin = {}
    for lettre in url:
        lettre_bin[lettre] = ord(lettre)
    
    return lettre_bin

ascii_lettre = lettre_ascii(url)


def lettre_bin(lettre_ascii):
    #je convertis l'ascii en binaire
    suite_lettre_bin = ''
    for i in lettre_ascii.values():
        a = i
        b = 0
        while a != 0:
            b = a%2
            print(b)
            a = a//2
            suite_lettre_bin += str(b)
        suite_lettre_bin += " "

    #le binaire n'est pas dans le bons sens. Je dois le changer pour que le dernier devienne premier
    return suite_lettre_bin

print(lettre_bin(ascii_lettre))

#crée la matrice en 7x7 
def mat():
    matrice = []
    ligne = []

    for i in range(7):    
        ligne.append([0])
        matrice.append(ligne)
    
    for i in range(len(matrice)):
        print(matrice[i])

    return matrice
print(mat())