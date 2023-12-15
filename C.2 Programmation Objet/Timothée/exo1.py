from random import randint

def lite_de_boite(n):
    pass

class boite:
    def __init__(self,longueur,largeur, hauteur):
        self.longueur = longueur
        self.largeur = largeur
        self.hauteur = hauteur
    
    def get_volume(self):
        return (self.longueur*self.largeur*self.hauteur)
    
    def get_infos(self):
        return "longueur : " + str(self.longueur) + "\nlargeur : " + str(self.largeur) + "\nhauteur : " + str(self.hauteur)
    
def test_boite(b1,b2):
    if b1 > b2:
        return "la boite 1 est plus grande"
    elif b1 < b2:
        return "la boite 2 est plus grande"
    else:
        return "les deux font la meme taille"
    
def long(p:boite):
    return p.get_volume() 

boite1 = boite(randint(1,30),randint(1,30),randint(1,30))
boite2 = boite(randint(1,30),randint(1,30),randint(1,30))

print(test_boite(boite1.get_volume(), boite2.get_volume()))
print(long(boite1))

