texte = '''Thenceforth the knight’s career depended,
he would not have said on himself, but on God and
his lady: and if we may judge by the ordinary languageof the xlviiromances, his lady was often the object of
actual adoration, little differing from that he would haveaddressed to the saints in the hour of danger or of triumph.
Philosophic divines teach us that although the worship of the saints may become in practice a gross and degrading superstition,
it has in it an element of true, and in itself ennobling, faith in ideals of humanity more or less perfectly revealed in human
form: and so while we smile at the fictions of extravagant fancy in which the mediæval knight was wont to clothe his love,
and his professions of love, for his mistress, we cannot reasonably doubt that in the main,
and for that time of youthful imaginations rather than of sober reasonings, the knight was right.
When I think of what society was, and what it would still be, without the humanizing influences of womanhood and ladyhood,
and what it is by means of these, I say that the tree may be judged by its fruits, and that it is from a right noble stock,
rightly and wisely cultivated in the main, in those old days, that we are still gathering such noble fruits. Much evil there
was along with the good; and, what is worse, much confusion between good and evil. I need not tell the reader of chivalry romances,
or of Lord Tennyson’s reproductions of some of their incidents in modern form of thought as well as language, how painfully this
confusion defaces many of the fairest characters and most interesting tales of chivalry, while the historical records of the times
in which those romances were written and read show that the actual state of morals and manners exhibited the like confusions
of good and evil, in the ideals as well as in the conduct of life. But, as I have already observed, we see, at least in the romance
before us, the good contending with, and mastering the evil, and this not least in the end of the story of the guilty loves of
Guenever and Launcelot, the knight whose fame in romance perhaps surpasses that of Amadis,
though even mediæval morality was obliged to censure the constancy of Launcelot’s love,
while it might unhesitatingly extol that of Amadis.
'''


class huffman():
    
    def __init__(self,livre):
        
        self.dico = {}
        self.gauche = None
        self.droit = None
        self.livre = livre
        
        

    def lettre(self):
        l = []
        l_clean = []
        for i in self.livre:
            l.append(i)
        
        for i in range(len(l)):
            if l[i] not in l_clean:            
                l_clean.append(l[i])
        dic = []
        
        for i in range(len(l_clean)):
            temp = 0
            for j in self.livre:
                if j == l_clean[i]:
                    temp += 1
            dic.append(temp)
            
        for i in range(len(l_clean)):
            self.dico[l_clean[i]] = [dic[i]]
            
                
        for i in range(len(self.dico)):
            i_max = i
            for j in range(i+1,len(self.dico)):
                if self.dico[i][j] > i_max:
                    i_max = j
            
            self.dico[i][i_max], self.dico[i][j] = self.dico[i][j]
                
            
        return self.dico


    


    
a = huffman(texte)
print(a.lettre())


        
