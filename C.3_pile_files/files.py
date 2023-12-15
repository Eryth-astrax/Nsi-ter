class Pile:
    
    def __init__(self) -> None:
        self.donnees = []
        
    def est_vide(self):
        return len(self.donnees) == 0
    
    def empile(self, val):
        self.donnees.append(val)
        
    def depile(self):
        
        if not self.est_vide():
            return self.donnees.pop()
        
        else:
            return None
        
    def to_str(self) -> str:
        '''
        Méthode qui renvoie une chaine de caractère correspondant au contenu de la Pile.
        '''
        chaine = ""
        for val in self.donnees:
            chaine = chaine + str(val)
        return chaine

    def est_egale(self, pile2):
        '''
        Methode qui permet de tester l'égalité avec une autre pile passée en paramètre.
        Param pile2 (Pile)
        Return (Bool)
        '''
        pile2_inv = Pile()

        # Comparaison des éléments en dépilant pile2
        test = True
        if ( (self.est_vide() and not pile2.est_vide())
                or (not self.est_vide() and pile2.est_vide()) ) :
            test = False
        else:
            pos = len(self.donnees)-1
            while pos >= 0 and not pile2.est_vide():
                elt = self.donnees[pos]
                elt2 = pile2.depile()
                if elt != elt2:
                    test = False
                pile2_inv.empile(elt2)
                pos = pos - 1

            # Rempilage de pile2
            while not pile2_inv.est_vide():
                pile2.empile(pile2_inv.depile())

        return test

def nbre_1_n(n:int):
    pile_temp = Pile()
    for i in range(n):
        pile_temp.empile(i+1)
    return pile_temp

def transfert(Pa : Pile, Pb : Pile):
    while not Pb.est_vide():
        Pa.empile(Pb.depile())

#exemple 1:
p1 = nbre_1_n(6)
print(p1.donnees)
p2 = nbre_1_n(8)
print(p2.donnees)
transfert(p1,p2)
print(p1.donnees)
print(p2.donnees)
