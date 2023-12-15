from random import randint
class Joueur:
    def __init__(self, nom):
        self.__pdv = 50
        self.__nom = nom

    def attaque(self):
        degas_infliges = randint(1,10)
        return degas_infliges

    def defense(self,degats_recus):
        self.__pdv = self.__pdv - degats_recus
        if self.__pdv <= 0 :
            self.__pdv = 0

    def get_pdv(self):
        return self.__pdv

    def get_nom(self):
        return self.__nom
j1 = Joueur("Arthur")
j2 = Joueur("Lancelot")
while j1.get_pdv() > 0 and j2.get_pdv() > 0:
    j1.defense(j2.attaque())
    j2.defense(j1.attaque())
    print("----- Nouveau tour -----")
    print(j1.get_nom() + " a " + str(j1.get_pdv()) + " points de vie")
    print(j2.get_nom() + " a " + str(j2.get_pdv()) + " points de vie")